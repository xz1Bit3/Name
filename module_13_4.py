from symtable import Class

from lib2to3.btm_utils import tokens
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

api = ''
bot = Bot(token =api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Калории')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()

    @dp.message_handler(state=UserState.weight)
    async def send_calories(message, state):
        await state.update_data(weight=message.text)
        data = await state.get_data()
        age = int(data['age'])
        growth = int(data['growth'])
        weight = int(data['weight'])

        calories_m = 10 * weight + 6.25 * growth - 5 * age + 5
        calories_w = 10 * weight + 6.25 * growth - 5 * age - 161
        await message.answer(f'Ваша норма калорий - {calories_m}, если вы мужчина\n '
                             f'                  '
                             f'                   -   {calories_w}, если вы женщина')

        await state.finish()






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates =True)