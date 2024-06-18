from aiogram import Router, F, types
from aiogram.filters.command import Command
from config import database


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
    genre = message.text.capitalize() # одно из genres
    books = await database.fetch("""
        SELECT * FROM books 
        INNER JOIN genres ON books.genre_id = genres.id
        WHERE genres.name = ?
    """, (genre,))
    # print(books)
    await message.answer(f"Книги из жанра {genre}", reply_markup=kb)
    for book in books:
        photo = types.FSInputFile(book["image"])
        await message.answer_photo(
            photo=photo,
            caption=f"{book['name']} - {book['price']} сом"
        )
    # await database.fetch("SELECT * FROM survey_results")


