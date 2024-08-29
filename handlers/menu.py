from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from loader import dp, db_session
from utils.db_api.models import User
import requests
from states.selectRegion import SelectRegion
from keyboards.default.menuKeyboard import menu, yes_or_no


async def get_prayer_times(city: str):
    """Fetch prayer times from API."""
    response = requests.get(f'https://islomapi.uz/api/present/day?region={city}')
    if response.status_code == 200:
        return response.json()
    return None


async def format_prayer_times(city: str, prayer_times: dict):
    """Format prayer times for user display."""
    date_str = prayer_times['date']
    year, month, day = date_str.split('-')
    month_names_uz = {
        '01': 'yanvar', '02': 'fevral', '03': 'mart', '04': 'aprel',
        '05': 'may', '06': 'iyun', '07': 'iyul', '08': 'avgust',
        '09': 'sentabr', '10': 'oktabr', '11': 'noyabr', '12': 'dekabr'
    }
    formatted_date = f"{int(day)}-{month_names_uz[month]}"

    return (
        f"🏙️<b>Shahar</b>: {city}\n\n"
        f"📅<b>Bugun {formatted_date}</b>\n\n"
        f"<b>Hafta kuni</b>: {prayer_times['weekday']}\n\n"
        f"<b>☪️Namoz vaqtlari</b>\n\n"
        f"<b>Bomdod</b>: {prayer_times['times']['tong_saharlik']}\n"
        f"<b>Quyosh</b>: {prayer_times['times']['quyosh']}\n"
        f"<b>Peshin</b>: {prayer_times['times']['peshin']}\n"
        f"<b>Asr</b>: {prayer_times['times']['asr']}\n"
        f"<b>Shom</b>: {prayer_times['times']['shom_iftor']}\n"
        f"<b>Hufton</b>: {prayer_times['times']['hufton']}\n\n"
        f"<b>Manba:</b> islom.uz\n\n"
    )


async def handle_prayer_times(message: Message, city: str):
    """Handle the 'today' and 'changecity' commands."""
    prayer_times = await get_prayer_times(city)
    if prayer_times:
        formatted_text = await format_prayer_times(city, prayer_times)
        await message.answer(formatted_text, reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Namoz vaqtlari uchun ma'lumotni olishda xato yuz berdi.")


@dp.message_handler(Command('today'))
async def handle_today(message: Message):
    user = db_session.query(User).filter_by(telegram_id=message.from_user.id).first()
    if user and user.city:
        await handle_prayer_times(message, user.city)
    else:
        await message.answer("Shahar tanlanmagan. Iltimos, shaharni tanlang.")


@dp.message_handler(Command('allownotify'))
async def handle_allownotify(message: Message):
    await SelectRegion.is_notify.set()
    await message.answer("Xar bir namoz vaqtida eslataylikmi?", reply_markup=yes_or_no)


@dp.message_handler(state=SelectRegion.is_notify)
async def handle_notification_preference(message: Message, state: FSMContext):
    user_response = message.text.lower()
    user = db_session.query(User).filter_by(telegram_id=message.from_user.id).first()

    if user_response in ["ha", "yes"]:
        if user:
            user.notify = True
            db_session.commit()
        await message.answer("Bot sizga xar bir namoz paytida xabar jo'natadi!", reply_markup=ReplyKeyboardRemove())
    elif user_response in ["yo'q", "no"]:
        if user:
            user.notify = False
            db_session.commit()
        await message.answer("Bot xabar yubormaydi.", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Iltimos, 'Ha' yoki 'Yo'q' deb javob bering.", reply_markup=yes_or_no)
        return

    await state.finish()


@dp.message_handler(Command('changecity'))
async def show_menu(message: Message):
    await SelectRegion.region.set()
    await message.answer('Shaharni tanlang', reply_markup=menu)


@dp.message_handler(state=SelectRegion.region)
async def send_times(message: Message, state: FSMContext):
    selected_city = message.text
    await message.answer(f'{selected_city} shahri tanlandi!')

    user = db_session.query(User).filter_by(telegram_id=message.from_user.id).first()
    if not user:
        user = User(telegram_id=message.from_user.id, city=selected_city)
        db_session.add(user)
    else:
        user.city = selected_city
    db_session.commit()

    await handle_prayer_times(message, selected_city)
    await message.answer("Xar bir namoz vaqtida eslataylikmi?", reply_markup=yes_or_no)
    await SelectRegion.is_notify.set()
