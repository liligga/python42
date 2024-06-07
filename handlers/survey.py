from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


survey_router = Router()


# FSM - Finite State Machine - конечный автомат
class BookSurvey(StatesGroup):
    name = State() # имя
    age = State() # возраст
    gender = State() # пол
    genre = State() # жанр


# "/opros"
@survey_router.message(Command("opros"))
async def start_opros(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.name) # устанавливаем состояние
    await message.answer("Вы можете остановить опрос в любой момент написав 'стоп'")
    await message.answer("Как Вас зовут?")

# "/stop"
@survey_router.message(Command("stop"))
@survey_router.message(F.text == "стоп")
async def stop_opros(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо! Ваш опрос закончен.")


@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    print("Имя:", message.text)
    await state.update_data(name=message.text)
    await state.set_state(BookSurvey.age)
    await message.answer("Сколько Вам лет?")


@survey_router.message(BookSurvey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Вводите только цифры!")
        return
    age = int(age)
    if age < 10 or age > 80:
        await message.answer("Возраст должен быть от 10 до 80 лет!")
        return
    await state.update_data(age=age)
    await state.set_state(BookSurvey.gender)
    await message.answer("Укажите Ваш пол?")


@survey_router.message(BookSurvey.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(BookSurvey.genre)
    await message.answer("Какой Ваш любимый жанр худ лит-ры?")


@survey_router.message(BookSurvey.genre)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)

    # берем сохраненные данные
    data = await state.get_data()
    print(data)
    # сохранение data в БД
    await state.clear()
    await message.answer("Спасибо за пройденный опрос!")