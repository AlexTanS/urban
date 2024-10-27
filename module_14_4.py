from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup

from crud_functions import *

all_products = get_all_products()  # получаю все записи из БД

token = ""
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Рассчитать"), KeyboardButton("Информация")],
        [KeyboardButton("Купить")]
    ],
    resize_keyboard=True
)
kb_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Продукт 1", callback_data="product_buying"),
         InlineKeyboardButton(text="Продукт 2", callback_data="product_buying"),
         InlineKeyboardButton(text="Продукт 3", callback_data="product_buying"),
         InlineKeyboardButton(text="Продукт 4", callback_data="product_buying")],
    ]
)


class UserState(StatesGroup):
    age = State()  # возраст
    growth = State()  # рост
    weight = State()  # вес


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет, я бот, помогающий твоему здоровью", reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer("Введите свой возраст(лет):")
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


# ================= Измененная функция ========================================
@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for product in all_products:
        with open("tablet.png", "rb") as img:
            await message.answer(text=f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")
            await message.answer_photo(img)
    await message.answer(text="Выберите продукт для покупки:", reply_markup=kb_inline)


# =============================================================================

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer(text="Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler()
async def start(message):
    await message.answer("Введите команду /start чтобы начать общение")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
