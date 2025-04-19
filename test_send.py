import asyncio
from aiogram import Bot
from data.config import BOT_TOKEN

async def test_send_message():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(12312312, "Test Namoz vaqti!⏰ (15:30)")
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(test_send_message())
