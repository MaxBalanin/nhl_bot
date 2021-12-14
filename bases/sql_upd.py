# # -*- coding: UTF-8 -*-
import sqlite3
from datetime import datetime, timedelta


def save_players_stats_2_zachitnic():
    with sqlite3.connect(f'bases/data/database.db') as conn:
        txt = open('bases/sql/zachitnic.txt', 'r')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS players_stats_2_zachitnic;')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS players_stats_2_zachitnic(Команда, Очки, Голы, Передачи,  Броски_в_створ_ворот,'
            ' Реализация_бросков_голы_броски, Штрафные_минуты,Время_на_площадке, Отборы_шайбы, '
            'Потери_шайбы,Силовые_приемы, Блокированные_броски, Выигранные_вбрасывания ,Проигранные_вбрасывания);')
        data = cursor.execute(txt.read()).fetchall()
        for i in data:
            print(i)
            set_players_stats_2_zachitnic(i)


def set_players_stats_2_zachitnic(lst):
    with sqlite3.connect(f'bases/bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO players_stats_2_zachitnic VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', lst)
        conn.commit()


def save_players_stats_2_napadenie():
    with sqlite3.connect(f'bases/data/database.db') as conn:
        txt = open('bases/sql/napadenie.txt', 'r')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS players_stats_2_napadenie;')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS players_stats_2_napadenie(Команда, Очки, Голы, Передачи,  Броски_в_створ_ворот,'
            ' Реализация_бросков_голы_броски, Штрафные_минуты,Время_на_площадке, Отборы_шайбы, '
            'Потери_шайбы,Силовые_приемы, Блокированные_броски, Выигранные_вбрасывания ,Проигранные_вбрасывания);')
        data = cursor.execute(txt.read()).fetchall()
        for i in data:
            print(i)
            set_players_stats_2_napadenie(i)


def set_players_stats_2_napadenie(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO players_stats_2_napadenie VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', lst)
        conn.commit()


def save_nap_v_nap():
    with sqlite3.connect(f'bases/data/database.db') as conn:
        txt = open('bases/sql/nap_v_nap.txt', 'r')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS nap_v_nap;')
        cursor.execute('CREATE TABLE IF NOT EXISTS nap_v_nap(Дата, Дома, doma, Дома_Голы, В_гостях_Голы, Условия_победы, В_гостях, gost);')
        data = cursor.execute(txt.read()).fetchall()
        for i in data:
            set_nap_v_nap(i)
        print('Успех!')


def set_nap_v_nap(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO nap_v_nap VALUES(?, ?, ?, ?, ?, ?, ?, ?)', lst)
        conn.commit()


def save_nap_v_zach():
    with sqlite3.connect(f'bases/data/database.db') as conn:
        txt = open('bases/sql/nap_v_zach.txt', 'r')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS nap_v_zach;')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS nap_v_zach(Дата, Дома, doma, Дома_Голы, В_гостях_Голы, Условия_победы, В_гостях, gost);')
        data = cursor.execute(txt.read()).fetchall()
        for i in data:
            set_nap_v_zach(i)
        print('Успех!')


def set_nap_v_zach(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO nap_v_zach VALUES(?, ?, ?, ?, ?, ?, ?, ?)', lst)
        conn.commit()


def save_zach_v_nap():
    with sqlite3.connect(f'bases/data/database.db') as conn:
        txt = open('bases/sql/zach_v_nap.txt', 'r')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS zach_v_nap;')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS zach_v_nap(Дата, Дома, doma, Дома_Голы, В_гостях_Голы, Условия_победы, В_гостях, gost);')
        data = cursor.execute(txt.read()).fetchall()
        for i in data:
            set_zach_v_nap(i)
        print('Успех!')


def set_zach_v_nap(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO zach_v_nap VALUES(?, ?, ?, ?, ?, ?, ?, ?)', lst)
        conn.commit()


def save_zach_v_zach():
    with sqlite3.connect(f'bases/data/database.db') as conn:
        txt = open('bases/sql/zach_v_zach.txt', 'r')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS zach_v_zach;')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS zach_v_zach(Дата, Дома, doma, Дома_Голы, В_гостях_Голы, Условия_победы, В_гостях, gost);')
        data = cursor.execute(txt.read()).fetchall()
        for i in data:
            set_zach_v_zach(i)
        print('Успех!')


def set_zach_v_zach(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO zach_v_zach VALUES(?, ?, ?, ?, ?, ?, ?, ?)', lst)
        conn.commit()


def save_vrat():
    with sqlite3.connect(f'bases/data/database.db') as conn:
        txt = open('bases/sql/vrat.txt', 'r')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS vrat;')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS vrat(Дата, Дома, doma, Дома_Голы, В_гостях_Голы, Условия_победы, В_гостях, gost);')
        data = cursor.execute(txt.read()).fetchall()
        for i in data:
            set_vrat(i)
        print('Успех!')


def set_vrat(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO vrat VALUES(?, ?, ?, ?, ?, ?, ?, ?)', lst)
        conn.commit()


def save_sp_all():
    with sqlite3.connect(f'bases/data/database.db') as conn:
        txt = open('bases/sql/sp_all.txt', 'r')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS sp_all;')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS sp_all(Дата, Дома, doma, Дома_Голы, В_гостях_Голы, Условия_победы, В_гостях, gost);')
        data = cursor.execute(txt.read()).fetchall()
        for i in data:
            set_sp_all(i)
        print('Успех!')


def set_sp_all(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO sp_all VALUES(?, ?, ?, ?, ?, ?, ?, ?)', lst)
        conn.commit()


def save_res():
    with sqlite3.connect(f'bases/data/database.db') as conn:
        txt = open('bases/sql/res.txt', 'r')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS res;')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS res(Дата, НЗ_Дома, НН_Дома, ЗН_Дома, ЗЗ_Дома, В_Дома, СП_Дома, Дома, Дома_Голы,'
            ' В_гостях_Голы, Условия_победы,'
            ' В_гостях, НЗ_Гость, НН_Гость, ЗН_Гость, ЗЗ_Гость, В_Гость, СП_Гость);')
        data = cursor.execute(txt.read()).fetchall()
        for i in data:
            set_res(i)

        print('Успех!')


def set_res(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO res VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', lst)
        conn.commit()


def save_all():
    print('Обработка nap_v_nap...')
    save_nap_v_nap()
    print('Обработка nap_v_zach...')
    save_nap_v_zach()
    print('Обработка zach_v_nap...')
    save_zach_v_nap()
    print('Обработка zach_v_zach...')
    save_zach_v_zach()
    print('Обработка vrat...')
    save_vrat()
    print('Обработка sp_all...')
    save_sp_all()
    print('Обработка res...')
    save_res()


def get_today():
    with sqlite3.connect(f'bases/data/database.db') as conn:
        tomorrow = datetime.now() + timedelta(days=1)
        cursor = conn.cursor()
        data = cursor.execute('SELECT * FROM res WHERE Дата = "{}"'.format(datetime.strftime(tomorrow, '%d.%m.%Y.'))).fetchall()
        for i in data:
            print(i)


