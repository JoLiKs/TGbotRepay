from aiogram import types

from lang import lang


become_driver_kb = [
        [types.KeyboardButton(text='Стать водителем')]
    ]
become_driver_kb = types.ReplyKeyboardMarkup(keyboard=become_driver_kb, resize_keyboard=True)

def cancel_kb(lang_p):
    cancel_kb = [
        [types.KeyboardButton(text=lang['in_main_menu'][lang_p])],
    ]
    return types.ReplyKeyboardMarkup(keyboard=cancel_kb, resize_keyboard=True)

shift_out_kb = [
        [types.KeyboardButton(text="Поставить статус занят")],
        [types.KeyboardButton(text="Закрыть смену"), types.KeyboardButton(text="Отправить геолокацию", request_location=True)]
]
shift_out_kb = types.ReplyKeyboardMarkup(keyboard=shift_out_kb, resize_keyboard=True)

join_kb = [
        [types.KeyboardButton(text="Участвовать")],
]
join_kb = types.ReplyKeyboardMarkup(keyboard=join_kb, resize_keyboard=True)


