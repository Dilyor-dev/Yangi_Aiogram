from aiogram.types import CallbackQuery

from loader import dp
from keyboards.default.python import buttons


@dp.callback_query_handler(text = '1-Dars')
async def dars_1(call:CallbackQuery):
    await call.message.answer("💻ⲢⲨⲦⲎⲞⲚ Ⲃⲟⲩⲓⲥⲏⲁ 1-ⲇⲁʀⲋⲓⲙⲓⲍⲛⲓ ⲕⲟʀⲓⲋⲏ υⲥⲏυⲛ ⲃⲓⲍⲛⲓⲛⳋ ⲕⲁⲛⲁⳑⲓⲙⲓⲍⳋⲁ ⲁ'ⲍⲟ ⲃⲟⳑⲓⲛⳋ!👇\n",reply_markup=buttons)
    await call.answer(cache_time=60)