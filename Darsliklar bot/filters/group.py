from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class Group(BoundFilter):
    async def check(self,message:types.Message):
        azo = await message.chat.get_member(message.from_user.id)
        return message.chat.type in (types.ChatType.GROUP,types.ChatType.SUPERGROUP)