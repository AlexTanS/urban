from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

token = ""
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = InlineKeyboardMarkup(resize_keyboard=True)

button_calories = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
button_formulas = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
kb.add(button_calories)
kb.add(button_formulas)


class UserState(StatesGroup):
    age = State()  # возраст
    growth = State()  # рост
    weight = State()  # вес


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb)


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет, я бот, помогающий твоему здоровью", reply_markup=kb)


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст(лет):")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост(см):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес(кг):")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = 10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) + 5
    await message.answer(f"Ваша норма калорий(для мужчин):{result}")
    await state.finish()


@dp.message_handler()
async def start(message):
    await message.answer("Введите команду /start чтобы начать общение")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
