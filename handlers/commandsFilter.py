from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp

@dp.message_handler(Command('changecity'))
async def changeCity(message: types.Message):
    await message.answer(f'Shahar  o\'zgardi')