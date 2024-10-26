import asyncio
import datetime
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.strategy import FSMStrategy
from keys import token

bot = Bot(token=token)


admin_chatid = 10

dp = Dispatcher(fsm_strategy=FSMStrategy.GLOBAL_USER)

logging.basicConfig(level=logging.INFO)


started = False
async def scheduled(wait_for):
    while True:
        now = datetime.datetime.now().time()
        await asyncio.sleep(wait_for)
        global started
        if not started:
            driver_reg(dp, bot)
            started = True
        if now.minute == 40 and now.hour == 9 and now.second == 1:
            pass


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(1))
    try:
        loop.run_until_complete(dp.start_polling(bot))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

