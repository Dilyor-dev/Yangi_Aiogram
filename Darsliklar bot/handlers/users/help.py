from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


from keyboards.default.contact import contact_buttons
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
    await message.answer('Tel nomerizi yoki locatsiyezi qoldirib keting!',reply_markup=contact_buttons)
