from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand('changecity', 'shaharni o\'zgartirish'),
            types.BotCommand('today', 'bugungi to\'liq taqvim'),
            types.BotCommand('allownotify', 'namoz vaqtida eslatish'),
        ]
    )
