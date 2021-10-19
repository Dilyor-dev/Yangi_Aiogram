from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


button = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text='CHECK',callback_data='check')
                        ]

                    ]
                )