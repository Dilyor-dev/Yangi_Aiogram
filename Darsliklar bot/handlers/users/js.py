from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.js_buttons import js_buttons
from loader import dp


@dp.message_handler(text='JS')
async def bot_start(message: types.Message):
    await message.answer(f"{message.from_user.full_name} JS kursiga xush kelibsiz!\n",reply_markup=js_buttons)

