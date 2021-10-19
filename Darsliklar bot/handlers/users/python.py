from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.python_buttons import python_buttons
from loader import dp


@dp.message_handler(text='Python')
async def bot_start(message: types.Message):
    await message.answer(f"{message.from_user.full_name} Python kursiga xush kelibsiz!\n",reply_markup=python_buttons)

