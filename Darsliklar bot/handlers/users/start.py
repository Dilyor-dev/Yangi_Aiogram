from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.python import buttons
from loader import dp, db
from filters import Shaxsiy
from utils.db_api.sqlite_base import Database
@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    id = message.from_user.id
    try:
        db.add_user(id,ism)
    except Exception as s:
        print(s)
    await message.answer(f"Salom, {message.from_user.full_name}!\n")
    await message.answer('💻𝑀𝐸𝑁𝑌𝑈⌨',reply_markup=buttons)
