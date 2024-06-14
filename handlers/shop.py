from aiogram import Router, F, types
from aiogram.filters.command import Command
import sqlite3


shop_router = Router()


@shop_router.message(Command("magazin"))
async def show_shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Фантастика"),
            ],
            [
                types.KeyboardButton(text="Ужас"),
                types.KeyboardButton(text="Драма"),
            ],
            [
                types.KeyboardButton(text="Комедия")
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Выберите жанр", reply_markup=kb)


genres = ("фантастика", "драма", "ужас", "комедия")


@shop_router.message(F.text.lower().in_(genres))
async def show_books(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    genre = message.text # одно из genres
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    query = cursor.execute("SELECT * FROM books WHERE genre_id = 2")
    books = query.fetchall()
    print(books)
    await message.answer("Книги из жанра ", reply_markup=kb)
