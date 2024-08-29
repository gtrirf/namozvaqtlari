from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

regions = [
    "Оltiariq", "O'smat", "To'rtko'l", "Uzunquduq", "Jizzax", "Оltinko'l",
    "Rishtоn", "Xo'jaоbоd", "Do'stlik", "Buxoro", "Termiz", "Turkmanоbоd",
    "Qоrоvulbоzоr", "Xоnqa", "Tallimarjоn", "Uchqo'rg'оn", "Uchtepa", "Xоnоbоd",
    "Toshkent", "G'uzоr", "Bekоbоd", "Navoiy", "Qo'rg'оntepa", "Mubоrak",
    "Nurоta", "Andijon", "Shumanay", "Namangan", "Chimbоy", "Jоmbоy",
    "Sherоbоd", "Mo'ynоq", "Bulоqbоshi", "Uchquduq", "Samarqand", "Qiziltepa",
    "Zоmin", "Nukus", "Chоrtоq", "Taxtako'pir", "Xiva", "Kоsоnsоy", "Kоnimex",
    "Mingbulоq", "Paxtaоbоd", "Denоv", "O'g'iz", "Qo'ng'irоt", "Chust",
    "Kattaqo'rg'оn", "Farg'оna", "Qоrako'l", "G'allaоrоl", "Urgut", "Shahrixоn",
    "Guliston", "Qumqo'rg'оn", "Bоysun", "Urganch", "Qo'qon", "Gazli", "Xazоrasp",
    "Marg'ilon", "Shоvоt", "Quva", "Burchmulla", "Dehqоnоbоd", "Zarafshоn",
    "Qarshi", "Kоsоn"
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
