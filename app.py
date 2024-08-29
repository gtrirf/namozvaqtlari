from aiogram import executor
from loader import dp, close_db_session
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from scheduler import daily_task
import logging
import sys
from logging.handlers import RotatingFileHandler

async def on_startup(dispatcher):
    logging.info("Bot is starting up...")
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    daily_task()
    logging.info("Bot started successfully.")

async def on_shutdown(dispatcher):
    logging.info("Bot is shutting down...")
    close_db_session()
    logging.info("Bot shut down successfully.")

if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            RotatingFileHandler("bot.log", maxBytes=5000000, backupCount=5),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logging.info("Starting bot...")
    try:
        executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
