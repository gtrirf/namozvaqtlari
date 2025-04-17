from aiogram import types
from loader import dp, bot
from data.config import ADMINS
from utils.db_api.database import SessionLocal
from utils.db_api.models import User


@dp.callback_query_handler(lambda c: c.data == "users")
async def show_users(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) not in ADMINS:
        await callback_query.answer("Bu buyruq faqat adminlar uchun!", show_alert=True)
        return

    session = SessionLocal()
    try:
        users = session.query(User).all()
        if not users:
            await callback_query.message.answer("Foydalanuvchilar ro'yxati bo'sh.")
            return

        text = "📋 Foydalanuvchilar ro'yxati:\n\n"
        for user in users:
            text += f"🆔 ID: {user.id}\n"
            text += f"Telegram ID: {user.telegram_id}\n"

            try:
                chat = await bot.get_chat(user.telegram_id)
                text += f"Fullname: {chat.full_name}\n"
                text += f"Username: @{chat.username}\n" if chat.username else "Username: Noma'lum\n"
            except:
                text += "Fullname: Noma'lum\nUsername: Noma'lum\n"

            text += f"Shahar: {user.city or 'Nomaʼlum'}\n"
            text += f"Bildirishnoma: {'✅' if user.notify else '❌'}\n"
            text += "———————\n"

        await callback_query.message.answer(text)
    except Exception as e:
        await callback_query.message.answer(f"Xatolik yuz berdi: {e}")
    finally:
        session.close()
