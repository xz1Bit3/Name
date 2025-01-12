from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# записываем ключ
api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# обработка сообщений хендлеры
@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст")
    await UserState.age.set()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text = "Рассчитать")
button1 = KeyboardButton(text = "Информация")
#добавляем в клавиатуру
kb.add(button)
kb.add(button1)

menu = InlineKeyboardMarkup()
button2 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
button3 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas')
menu.add(button2)
menu.add(button3)

@dp.message_handler(text = "Рассчитать")
async def main_menu(message):
    await message.answer("Выбери опцию", reply_markup=menu)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()

@dp.message_handler(commands = ["start"])
async def Start_message(message):
    #reply_markup=kb показываем клавиатуру
    await message.answer("Привет! Я бот помогающий твоему здоровью", reply_markup=kb)

#обрабатываем кнопку
@dp.message_handler(text = "Рассчитать")
async def inform(message):
    await message.answer("Рассчитать")

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer("Введите свой рост")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer("Введите свой вес")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    st_1 = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    st_2 = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161)
    await message.answer(f'Ваша норма колорий:\n {st_1} ккал - для мужчин \n {st_2} ккал - для женщин ')
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)