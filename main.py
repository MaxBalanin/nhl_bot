# # -*- coding: UTF-8 -*-
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from app.cmd_start import register_fc
from app.cmd_admin import register_admin
from config import token
from bases import cmd_base


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/res", description="Узнать прогноз на сегодня."),
    ]
    await bot.set_my_commands(commands)


async def main():

    bot = Bot(token=token)
    dp = Dispatcher(bot, storage=MemoryStorage())
    register_admin(dp)
    register_fc(dp)
    print('start')

    await set_commands(bot)
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
