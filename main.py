import asyncio
import logging
from aiogram import types

from config import dp, bot, database
from handlers import (
    start_router,
    shop_router,
    survey_router,
    picture_router,
    mashina_router,
    echo_router
)


async def on_startup(bot):
    await database.create_tables()


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="magazin", description="Наши товары"),
        types.BotCommand(command="opros", description="Пройдите на опрос"),
        types.BotCommand(command="picture", description="Картинка"),
    ])
    # регистрируем роутер
    dp.include_router(picture_router)
    dp.include_router(start_router)
    dp.include_router(survey_router)
    dp.include_router(mashina_router)
    dp.include_router(shop_router)

    # в самом конце
    dp.include_router(echo_router)
    # запускаем бот
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())