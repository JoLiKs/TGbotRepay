import asyncio
import os
import random
from aiogram import F, types, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, Message, InputFile
from states import St
from keyboards import join_kb
from lang import lang, LangFilter
from aiolimiter import AsyncLimiter

router = Router()

admins = (0,)
bot: Bot


def limited_message(*args):
    def decorator(handler):
        @router.message(*args)
        async def wrapper(message: types.Message, state: FSMContext):
           # print(f"Получено сообщение: {message.text}")
            async with limiter:
                await handler(message, state)
        return wrapper

    return decorator


@limited_message(F.text == "/testo")
async def testo(message: types.Message, state: FSMContext):
    if message.from_user.id in admins:
        data = await state.get_data()

questions = ["surname", "name", "company", "position", "telegram_contact", "email"]


@limited_message(F.text == "/start")
async def start(message: types.Message, state: FSMContext):
    if message.from_user.username is None: return await message.answer(lang['not_tag']['ru'])
    await message.answer(lang['rules']['ru'], reply_markup=join_kb)


@limited_message(F.text, LangFilter('join'))
async def join(message: types.Message, state: FSMContext):
    if message.from_user.username is None: return await message.answer(lang['not_tag']['en'])
    await state.set_state(St.questions)



@limited_message(F.text == "")
async def busy(message: types.Message, state: FSMContext):
    if message.from_user.username is None: return await message.answer(lang['not_tag']['en'])
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



@limited_message(F.text)
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
