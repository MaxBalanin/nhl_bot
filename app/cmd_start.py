# # -*- coding: UTF-8 -*-
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as fmt
from git.nhl_bot.app import parse
from datetime import datetime


class StateMachine(StatesGroup):
    waiting_data = State()


async def get_start(message: types.Message):
    await message.answer('Привет, я даю прогнозы на исход матчей NHL.\n'
                         'Введи команду /today и всё узнай.')


async def get_fc(message: types.Message):
    await message.answer('До какого числа дать прогноз? (в формате дд.мм.гггг)')
    await StateMachine.waiting_data.set()


async def set_date(message: types.Message, state: FSMContext):
    try:
        await message.answer('Инфа загружается!')
        await state.update_data(date=message.text)
        user_data = await state.get_data()
        data = parse.get_all(user_data['date'])
        for i in data:
            w1 = round(i[5]/(i[5]+i[6])*100, 1)
            w2 = round(i[6]/(i[5]+i[6])*100, 1)
            await message.answer(f'{i[0]}\n'
                                 f'Шансы на победу:\n'
                                 f'{i[1]} {w1}%\n'
                                 f'{i[2]} {w2}%\n')
        await message.answer(f'Более подробные прогнозы ты можешь найти в нашей группе ВК{fmt.hide_link("https://vk.com/club209465257")}',
                             parse_mode=types.ParseMode.HTML)
    except Exception as e:
        await message.answer('Произошла ошибка, попробуйте ещё раз.')
        print('Ошибка бота', e)


async def get_today(message: types.Message):
    try:
        await message.answer('Инфа загружается!')
        data = parse.get_all(datetime.strftime(datetime.now(), '%d.%m.%Y'))
        # g = 0
        for i in data:
            # g += 1
            w1 = round(i[5]/(i[5]+i[6])*100, 1)
            w2 = round(i[6]/(i[5]+i[6])*100, 1)
            await message.answer(f'{i[0]}\n'
                                 f'Шансы на победу:\n'
                                 f'{i[1]} {w1}%\n'
                                 f'{i[2]} {w2}%\n')
            # if g == 3:
            #     break
        await message.answer(
            f'Более подробные прогнозы ты можешь найти в нашей группе ВК{fmt.hide_link("https://vk.com/club209465257")}',
            parse_mode=types.ParseMode.HTML)
    except Exception as e:
        await message.answer('Произошла ошибка, попробуйте ещё раз.')
        print('Ошибка бота', e)


def register_fc(dp: Dispatcher):
    dp.register_message_handler(get_start, commands="start")
    dp.register_message_handler(get_fc, commands="date", state="*")
    dp.register_message_handler(set_date, state=StateMachine.waiting_data)
    dp.register_message_handler(get_today, commands="today")