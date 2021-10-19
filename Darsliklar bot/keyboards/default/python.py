from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Python',),
            KeyboardButton(text='JS'),
        ],
        [
            KeyboardButton(text='Telegram Bot'),
        ],

    ],
    resize_keyboard=True
)