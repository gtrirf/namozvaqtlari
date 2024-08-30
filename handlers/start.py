from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from loader import dp
from states.selectRegion import SelectRegion
from keyboards.default.menuKeyboard import menu

@dp.message_handler(Command('start'))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await SelectRegion.region.set()
    await message.answer('Iltimos, shaharni tanlang:', reply_markup=menu)