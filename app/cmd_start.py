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



''' /START '''
async def get_start(message: types.Message):
    if cmd_base.check_user(message.from_user.id) == message.from_user.id:
        await message.answer('Привет, я даю прогнозы на исход матчей NHL.\n'
                             'Введи команду /res и всё узнай.')
    else:
        sevenday = datetime.now() + timedelta(days=5)
        cmd_base.ins_user_data(
            [message.from_user.id, message.from_user.username,
             datetime.strftime(datetime.now(), '%d.%m.%Y'),
             datetime.strftime(sevenday, '%d.%m.%Y')])
        await message.answer('Привет, я даю прогнозы на исход матчей NHL.\n'
                             'Введи команду /today и всё узнай.')



'''Команда чтобы узнать свой ид'''
async def get_id(message: types.Message):
    await message.answer(f'Ваш ID: {message.from_user.id}\nВаш никнейм: {message.from_user.username}')


# async def get_fc(message: types.Message):
#     await message.answer('До какого числа дать прогноз? (в формате дд.мм.гггг)')
#     await StateMachine.waiting_data.set()
#
#
# async def set_date(message: types.Message, state: FSMContext):
#     try:
#         await message.answer('Инфа загружается!')
#         await state.update_data(date=message.text)
#         user_data = await state.get_data()
#         data = parse.get_all(user_data['date'])
#         for i in data:
#             w1 = round(i[5]/(i[5]+i[6])*100, 1)
#             w2 = round(i[6]/(i[5]+i[6])*100, 1)
#             await message.answer(f'{i[0]}\n'
#                                  f'Шансы на победу:\n'
#                                  f'{i[1]} {w1}%\n'
#                                  f'{i[2]} {w2}%\n')
#         await message.answer(f'Более подробные прогнозы ты можешь найти в нашей группе ВК{fmt.hide_link("https://vk.com/club209465257")}',
#                              parse_mode=types.ParseMode.HTML)
#     except Exception as e:
#         await message.answer('Произошла ошибка, попробуйте ещё раз.')
#         await state.finish()
#         print('Ошибка бота', e)


''' Выдаёт прогноз по голосам на сайте '''
# async def get_today(message: types.Message):
#     try:
#         cmd_base.user_log([message.from_user.id, message.from_user.username, datetime.strftime(datetime.now(), '%d.%m.%Y'), '/today'])
#         await message.answer('Инфа загружается!')
#         data = parse.get_all(datetime.strftime(datetime.now(), '%d.%m.%Y'))
#         for i in data:
#             w1 = round(i[5]/(i[5]+i[6])*100, 1)
#             w2 = round(i[6]/(i[5]+i[6])*100, 1)
#             await message.answer(f'{i[0]}\n'
#                                  f'Шансы на победу:\n'
#                                  f'{i[1]} {w1}%\n'
#                                  f'{i[2]} {w2}%\n')
#         await message.answer(
#             f'Более подробные прогнозы ты можешь найти в нашей группе ВК {"https://vk.com/club209465257"}',
#             )
#     except Exception as e:
#         await message.answer('Произошла ошибка, попробуйте ещё раз.')
#         print('Ошибка бота', e)


''' Выдаёт прогноз из таблиц '''
async def get_today_res(message: types.Message):
    try:
        if cmd_base.check_privileges(message.from_user.id):
            tomorrow = datetime.now() + timedelta(days=1)
            cmd_base.user_log(
                [message.from_user.id, message.from_user.username, datetime.strftime(datetime.now(), '%d.%m.%Y'), '/res'])
            await message.answer('Инфа загружается!')
            data = cmd_base.get_res(datetime.strftime(tomorrow, '%d.%m.%Y.')) # Достаём данные из базы
            cmd_base.save_res_log(data) # Сохраняем в базу логов
            await message.answer('Дата, НЗ_Дома, НН_Дома, ЗН_Дома, ЗЗ_Дома, В_Дома, СП_Дома, Дома, Дома_Голы, '
                                 ' В_гостях_Голы, Условия_победы,'
                                 ' В_гостях, НЗ_Гость, НН_Гость, ЗН_Гость, ЗЗ_Гость, В_Гость, СП_Гость')
            for i in data:
                await message.answer(i)
        else:
            await message.answer('Плати шекели!!!')
    except Exception as e:
        await message.answer('Произошла ошибка, попробуйте ещё раз.')
        print('Ошибка бота get_today_res', e)


def register_fc(dp: Dispatcher):
    dp.register_message_handler(get_start, commands="start")
    dp.register_message_handler(get_id, commands="id")
    # dp.register_message_handler(get_fc, commands="date", state="*")
    # dp.register_message_handler(set_date, state=StateMachine.waiting_data)
    # dp.register_message_handler(get_today, commands="today")
    dp.register_message_handler(get_today_res, commands="res")