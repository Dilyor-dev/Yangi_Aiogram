import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message,CallbackQuery

from data.config import ADMINS,Kanalar
from keyboards.inline.post_buttons import confirmation_button, post_callback
from loader import dp,bot
from states.holatlar import NewPost

@dp.message_handler(commands='new_post')
async def new_post(message:types.Message):
    await message.answer(text='New post yuboring!')
    await NewPost.NewMessage.set()
@dp.message_handler(state=NewPost.NewMessage)
async def new_message(message: Message,state:FSMContext):
    await state.update_data(text=message.html_text,mention = message.from_user.get_mention())
    await message.answer(text=f"Postni tasdiqlash uchun yuboraymi?",reply_markup=confirmation_button)

    await NewPost.next()

@dp.callback_query_handler(post_callback.filter(action="post"),state=NewPost.Confirm)
async def confirm_post(call:CallbackQuery,state: FSMContext):
    async with state.proxy() as data:
        text = data.get('text')
        mention = data.get('mention')
    await state.finish()
    await call.message.delete()
    await call.message.answer('Post adminga yuborildi')
    await bot.send_message(ADMINS[0],f"Foydalanuvchi {mention} quyidagi postni new post qimoqchi!")
    await bot.send_message(ADMINS[0],text,parse_mode='HTML',reply_markup=confirmation_button)

@dp.callback_query_handler(post_callback.filter(action='cancel'),state=NewPost.Confirm)
async def post_cancel(call:CallbackQuery,state:FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Post rad etildi!')

@dp.message_handler(state=NewPost.Confirm)
async def post_unknown(message:Message):
    await message.answer('NEw post qilish yoki rad etishni tanlang!')

@dp.callback_query_handler(post_callback.filter(action="post"),user_id = ADMINS)
async def approve_test(call:CallbackQuery):
    await call.answer('New postga ruhsat berdingiz',show_alert=True)
    target_channel = Kanalar[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)

@dp.callback_query_handler(post_callback.filter(action='cancel'),user_id = ADMINS)
async def decline_test(call:CallbackQuery):
    await call.answer('Post rad etildi',show_alert=True)
    await call.message.edit_reply_markup()