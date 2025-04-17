from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile
from data.config import ADMINS
from keyboards.inline.admin_panel import admin_keyboards
import os

@dp.message_handler(Command("admin_panel"))
async def admin_panel(message: types.Message):
    if str(message.from_user.id) not in ADMINS:
        await message.reply("Kechirasiz, sizda ushbu buyruqni ishlatishga ruxsat yo'q.")
        return

    await message.reply("Admin panel:", reply_markup=admin_keyboards)

@dp.callback_query_handler(lambda c: c.data == "get_logs")
async def callback_get_log(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) not in ADMINS:
        await callback_query.answer("Kechirasiz, sizda ushbu buyruqni ishlatishga ruxsat yo'q.", show_alert=True)
        return

    log_file_path = "bot.log"

    if not os.path.exists(log_file_path):
        await callback_query.message.reply("Log fayli topilmadi.")
        return

    try:
        log_file = InputFile(log_file_path)
        await callback_query.message.answer_document(log_file)
    except Exception as e:
        await callback_query.message.reply(f"Xatolik yuz berdi: {str(e)}")
