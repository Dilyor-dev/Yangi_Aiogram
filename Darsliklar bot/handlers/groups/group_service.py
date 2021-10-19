from aiogram import types
from filters import Group
from loader import dp,bot

@dp.message_handler(Group(),content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_member(message:types.Message):
    members = ",".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f'Gruppaga xush kelibsiz,{members} !')


@dp.message_handler(Group(),content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def left_member(message:types.Message):
    if message.left_chat_member == message.from_user.id:
        await message.answer(f" guruhni tark etdi {message.left_chat_member} ")
    else:
        await message.answer(f"{message.left_chat_member.full_name} guruhdan haydaldi ADMIN {message.from_user.get_mention(as_html=True)}. ")