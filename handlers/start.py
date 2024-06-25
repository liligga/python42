import asyncio
from aiogram import Router, types, F
from aiogram.filters.command import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    # print("Message", message)
    # print("User info", message.from_user)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")
            ],
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/geekskg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/geekskg")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about")
            ],
            [
                types.InlineKeyboardButton(text="Пожертвуйте нам", callback_data="donate")
            ]
        ]
    )
    name = message.from_user.first_name
    await message.answer(
        f"Привет, {name}",
        reply_markup=kb
    )


@start_router.callback_query(F.data == "subscription")
async def about_handler(callback: types.CallbackQuery):
    await callback.answer() # для того чтобы бот не зависал
    # await asyncio.sleep(10)
    await callback.message.answer("О нас")


@start_router.callback_query(F.data == "donate")
async def about_handler(callback: types.CallbackQuery):
    await callback.answer() # для того чтобы бот не зависал
    await callback.message.answer("Мы будем очень благодарны за вашу помощь")