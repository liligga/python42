from aiogram import Router, types
from aiogram.filters.command import Command


picture_router = Router()


@picture_router.message(Command("picture"))
async def picture_handler(message: types.Message):
    file = types.FSInputFile("images/cat.jpg")
    # await message.answer_photo(photo=file, caption="Котик")
    await message.reply_photo(photo=file, caption="Котик")
