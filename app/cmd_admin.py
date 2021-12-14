# # -*- coding: UTF-8 -*-
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as fmt
from datetime import datetime, timedelta
import sqlite3
from bases import cmd_base


class StateMachine(StatesGroup):
    waiting_data = State()


async def get_update(message: types.Message):
    try:
        if message.from_user.id in []:
            await message.answer('Обновление запущено, ожидайте...')
            cmd_base.upd_all()
            await message.answer('Обновление прошло успешно!')
        else:
            await message.answer('У тебя здесь нет власти!')
    except Exception as e:
        await message.answer(f'Мы обосрались: {e}')


async def get_upd_ud(message: types.Message):
    await message.answer('ИД/Никнейм пользователя и сколько дней через пробел.')
    await StateMachine.waiting_data.set()


async def set_date(message: types.Message, state: FSMContext):
    try:
        if message.from_user.id in []:
            await state.update_data(inf=message.text)
            user_data = await state.get_data()
            inform = user_data['inf'].split()
            if inform[0].isdigit():
                cmd_base.upd_ud_id(inform[0], inform[1])
            else:
                cmd_base.upd_ud_un(inform[0], inform[1])
            await message.answer('Данные изменены!')
    except Exception as e:
        await message.answer('Произошла ошибка, попробуйте ещё раз.')
        await state.finish()
        print('Ошибка бота set_date', e)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(get_update, commands="update_base")
    dp.register_message_handler(get_upd_ud, commands="user_upd", state='*')
    dp.register_message_handler(set_date, state=StateMachine.waiting_data)