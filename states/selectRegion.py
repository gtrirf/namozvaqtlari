from aiogram.dispatcher.filters.state import StatesGroup, State


class SelectRegion(StatesGroup):
    region = State()
    is_notify = State()

