# # -*- coding: UTF-8 -*-
import asyncio
from bases import commands_stats
from bases import player
from bases import timetable
from bases import players2
from bases import base
from bases import sql_upd
from bases import forecast
from datetime import datetime, timedelta


def save_all():
    '''
    save
    Админская команда
    '''
    commands_stats.save_commands_stats()
    player.save_pstats()
    timetable.save_timetable()
    players2.get_list()
    players2.save_pstats2()
    print('Данный успешно сохранены!!!!')


def upd_all():
    '''
    upd
    Админская команда
    '''
    # commands_stats.upd_commands_stats()
    # player.upd_pstats()
    # timetable.upd_timetable()
    # players2.get_list()
    # players2.upd_pstats2()
    sql_upd.save_all()
    # forecast.save_all()
    print('Данный успешно обновлены!!!!')


def ins_user_data(lst):
    '''
    Добавить пользователя в базу
    :param lst:
    :return:
    '''
    try:
        base.set_user_data(lst)
    except Exception as e:
        print(f'Мы обосрались ins_user_data: {e}')


def check_user(user):
    '''
    Проверка пользователя в базе
    :param id:
    :return:
    '''
    try:
        user_id = base.get_user_data(user)
        if not user_id:
            return None
        else:
            return user_id[0][0]
    except Exception as e:
        print(f'Мы обосрались check_user: {e}')


def check_privileges(user):
    '''
    Проверка пользователя в базе
    :param id:
    :return:
    '''
    try:
        user_data = base.get_user_data(user)
        if not user_data:
            return False
        else:
            if datetime.strptime(user_data[0][3], '%d.%m.%Y') >= datetime.strptime(datetime.strftime(datetime.now(), '%d.%m.%Y'), '%d.%m.%Y'):
                return True
            else:
                print(datetime.strptime(user_data[0][3], '%d.%m.%Y'), datetime.strptime(datetime.strftime(datetime.now(), '%d.%m.%Y'), '%d.%m.%Y'))
                return False
    except Exception as e:
        print(f'Мы обосрались check_privileges: {e}')


def upd_ud_id(user_id, days):
    '''
     продлить юзера по ИД
     Админская команда
     '''
    days = datetime.now() + timedelta(days=int(days))
    base.upd_user_data_on_id(user_id, datetime.strftime(days, '%d.%m.%Y'))


def upd_ud_un(username, days):
    '''
     продлить юзера по никнейму
     Админская команда
     '''
    days = datetime.now() + timedelta(days=int(days))
    base.upd_user_data_on_username(username, datetime.strftime(days, '%d.%m.%Y'))


def user_log(lst):
    '''
    Добавление действия пользователя в таблицу логов user_log
    :param lst:
    :return:
    '''
    try:
        base.set_user_log(lst)
    except Exception as e:
        print(f'Мы обосрались user_log: {e}')


def save_res_log(lst):
    '''
    Добавление прогноза в таблицу логов res_log
    :param lst:
    :return:
    '''
    try:
        base.set_res_log(lst)
    except Exception as e:
        print(f'Мы обосрались save_res_log: {e}')


def get_res(date):
    '''
    Достаём результаты из таблицы прогнозов
    :return:
    '''
    try:
        return base.get_res(date)
    except Exception as e:
        print(f'Мы обосрались get_res: {e}')