import asyncio
import datetime
import re

import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import Group,Admin
from loader import dp,bot

@dp.message_handler(Group(),Command("ban",prefixes="$/"),Admin())
async def only_read(message:types.Message):
    azo = message.reply_to_message.from_user
    azo_id = azo.id
    block = re.compile(r"($ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    blocked = block.match(message.text)
    vaqt = blocked.group(2)
    sababi = blocked.group(3)

    if not vaqt:
        vaqt = 5
    vaqt = int(vaqt)

    if not sababi:
        sababi = "Yoqmadi"

    block_vaqti = datetime.datetime.now() + datetime.timedelta(minutes=vaqt)

    await message.chat.restrict(user_id=azo_id,can_send_messages=False,until_date=block_vaqti)
    await message.answer(f'Foydalanuvchi {message.reply_to_message.from_user.username} {vaqt} minutga {sababi} ')

    await asyncio.sleep(5)
    await message.delete()