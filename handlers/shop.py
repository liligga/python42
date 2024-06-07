from aiogram import Router, F, types
from aiogram.filters.command import Command


shop_router = Router()


@shop_router.message(Command("magazin"))
async def show_shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Фантастика"),
            ],
            [
                types.KeyboardButton(text="Романтика"),
                types.KeyboardButton(text="Драма"),
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Выберите жанр", reply_markup=kb)


@shop_router.message(F.text == "Фантастика")
async def show_fantastika(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Книги из жанра Фантастика", reply_markup=kb)


@shop_router.message(F.text == "Романтика")
async def show_romantika(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Книги из жанра Романтика", reply_markup=kb)


@shop_router.message(F.text == "Драма")
async def show_drama(message: types.Message):
    
    await message.answer("Книги из жанра Драма")