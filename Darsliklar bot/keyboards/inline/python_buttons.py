from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

python_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1-Dars',callback_data='1-Dars'),
            InlineKeyboardButton(text='2-Dars',callback_data='2-Dars'),
        ],
        [
            InlineKeyboardButton(text='3-Dars',callback_data='3-Dars'),
            InlineKeyboardButton(text='4-Dars',callback_data='4-Dars'),
        ],
        [
            InlineKeyboardButton(text='Ulanish',switch_inline_query='Zor bot ekan!'),
            InlineKeyboardButton(text="Kanalimizga a'zo bolish",url='https://t.me/howdyho_official'),
        ]
    ],
    resize_keyboard=True
)