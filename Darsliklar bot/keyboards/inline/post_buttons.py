from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post","action")

confirmation_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text='✅Nice',callback_data=post_callback.new(action="post")),
        InlineKeyboardButton(text='❌NO',callback_data=post_callback.new(action="cancel")),
    ]]

)