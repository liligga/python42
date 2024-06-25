from aiogram import Router, F, types
from aiogram.filters.command import Command
from crawler.mashinakg import get_page, get_links


mashina_router = Router()


@mashina_router.message(Command("obyavlenia"))
async def show_obyavlenia(message: types.Message):
    await message.answer("https://www.house.kg/details/4793335f896ed8e4d1f4-26541312")