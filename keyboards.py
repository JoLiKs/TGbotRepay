from aiogram import types

from lang import lang


def cancel_kb(lang_p):
    cancel_kb = [
        [types.KeyboardButton(text=lang['in_main_menu'][lang_p])],
    ]
    return types.ReplyKeyboardMarkup(keyboard=cancel_kb, resize_keyboard=True)



join_kb = [
        [types.KeyboardButton(text="Участвовать")],
]
join_kb = types.ReplyKeyboardMarkup(keyboard=join_kb, resize_keyboard=True)


