from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("changecity", "Shaharni o‘zgartirish"),
            types.BotCommand("today", "Bugungi to‘liq taqvim"),
            types.BotCommand("allownotify", "Namoz vaqtida eslatish"),
        ]
    )
