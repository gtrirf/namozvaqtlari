from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

regions = [
    "Urgut", "To'rtko'l", "Jizzax",
    "Rishtоn", "Xo'jaоbоd", "Buxoro", "Termiz",
    "Uchqo'rg'оn", "Uchtepa", "Xоnоbоd",
    "Toshkent","Bekоbоd", "Navoiy",
    "Nurоta", "Andijon", "Shumanay", "Namangan", "Chimbоy", "Jоmbоy",
    "Mo'ynоq", "Uchquduq", "Samarqand",
    "Zоmin", "Nukus", "Chоrtоq", "Xiva", "Kоsоnsоy",
    "Denоv","Chust",
    "Kattaqo'rg'оn", "Farg'оna","Shahrixоn",
    "Guliston", "Urganch", "Qo'qon", "Gazli", "Xazоrasp",
    "Marg'ilon", "Zarafshоn",
    "Qarshi",
]

keyboard_rows = [[KeyboardButton(text=city)] for city in regions]

menu = ReplyKeyboardMarkup(
    keyboard=keyboard_rows,
    resize_keyboard=True,
    one_time_keyboard=True
)

yes_or_no = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard = [
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q")
        ],
    ]
)
