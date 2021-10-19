import asyncio
from aiogram.dispatcher import FSMContext
from aiogram import types
from states.holatlar import NewPost
from data.config import ADMINS
from loader import dp,bot,db

@dp.message_handler(text="/allusers",user_id =ADMINS)
async def get_all_users(message:types.Message,):
    users = db.select_all_users()
    await message.answer(users)

@dp.message_handler(text='/reklama',user_id =ADMINS)
async def send_add_to_all(message:types.Message,state: FSMContext):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id,text=f"nma gappp")
