import asyncio
import os
import random
from aiogram import F, types, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, Message, InputFile
from states import St
from keyboards import join_kb
from lang import lang, LangFilter

router = Router()

admins = (0,)
bot: Bot


@router.message(F.text == "/testo")
async def testo(message: types.Message, state: FSMContext):
    if message.from_user.id in admins:
        data = await state.get_data()

questions = ["surname", "name", "company", "position", "telegram_contact", "email"]


@router.message(F.text == "/start")
async def start(message: types.Message, state: FSMContext):
    if message.from_user.username is None: return await message.answer(lang['not_tag']['ru'])
    await message.answer(lang['rules']['ru'], reply_markup=join_kb)


@router.message(F.text, LangFilter('join'))
async def join(message: types.Message, state: FSMContext):
    if message.from_user.username is None: return await message.answer(lang['not_tag']['ru'])
    await state.set_state(St.questions)



@router.message(F.text == "")
async def busy(message: types.Message, state: FSMContext):
    if message.from_user.username is None: return await message.answer(lang['not_tag']['ru'])
    data = await state.get_data()




class AIter:  # упрощенный аналог range для async for
    def __init__(self, N):
        self.i = 0
        self.N = N

    def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.i
        # print(f"start {i}")

        await asyncio.sleep(0.7)
        # print(f"end {i}")
        if i >= self.N:
            raise StopAsyncIteration
        self.i += 1
        return i


clients = []



#
# @router.message(F.text, LangFilter('in_main_menu'))
# async def back_to_menu(message: Message, state: FSMContext):
#     print('exit in menu from func!')
#     data = await state.get_data()
#     await message.answer('Вы в главном меню', reply_markup=main_menu_kb)
#     return


@router.message(F.text)
async def other_text(message: Message, state: FSMContext):
    data = await state.get_data()
    f = open('logs.txt', 'a+', encoding='utf-8')
    f.write(
        f'msg from {f"@{message.from_user.username}" if not message.from_user.username is None else f"{message.from_user.id} {message.from_user.first_name}"}:\n{message.text}\n\n')
    f.close()


def repay_reg(dp, botik):
    global bot
    bot = botik
    dp.include_router(router)
