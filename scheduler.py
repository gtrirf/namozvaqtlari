from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
import requests
from datetime import datetime
from utils.db_api.models import User
from loader import bot, db_session
from datetime import datetime, timedelta


scheduler = AsyncIOScheduler()

async def send_prayer_notification(chat_id: int, prayer_name: str, prayer_time: str):
    await bot.send_message(
        chat_id=chat_id,
        text=f"{prayer_name} vaqti!⏰ ({prayer_time})",
        parse_mode="HTML"
    )

def schedule_daily_prayer_times(user: User):
    response = requests.get(f'https://islomapi.uz/api/present/day?region={user.city}')
    if response.status_code == 200:
        prayer_times = response.json()['times']

        for prayer_name, prayer_time in prayer_times.items():
            prayer_time_obj = datetime.strptime(prayer_time, "%H:%M").time()

            prayer_time_datetime = datetime.combine(datetime.today(), prayer_time_obj)

            notification_time = prayer_time_datetime - timedelta(minutes=10)

            scheduler.add_job(
                send_prayer_notification,
                'cron',
                hour=notification_time.hour,
                minute=notification_time.minute,
                args=[user.telegram_id, prayer_name, prayer_time]
            )
    else:
        print(f"Failed to  prayer times for user {user.telegram_id} from {user.city}")

def daily_task():
    users = db_session.query(User).filter_by(notify=True).all()

    for user in users:
        schedule_daily_prayer_times(user)

scheduler.start()

scheduler.add_job(daily_task, 'cron', hour=0, minute=0)
