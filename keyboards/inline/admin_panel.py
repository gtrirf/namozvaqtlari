from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



admin_keyboards = InlineKeyboardMarkup(row_width=1)
admin_keyboards.add(
    InlineKeyboardButton("Log faylini yuklab olish", callback_data="get_logs"),
    InlineKeyboardButton("Foydalanuvchilar ro'yxatini ko'rish", callback_data='users')
)