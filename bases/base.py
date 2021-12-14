# # -*- coding: UTF-8 -*-
import sqlite3
from datetime import datetime, timedelta


def create_table():
    with sqlite3.connect(f'bases/data/database.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS commands_stats(Дата, Команда, Всего_Сыгранные_матчи, Всего_Победы,'
                     ' Всего_Победы_в_овертайме, Всего_Победы_по_буллитам, Всего_Ничьи, Всего_Поражения_по_буллитам,'
                     ' Всего_Поражения_в_овертайме, Всего_Поражения, Всего_Набранные_очки, Всего_Заброшенные_шайбы,'
                     ' Всего_Пропущенные_шайбы, Всего_Разность_шайб, Всего_Штрафное_время,'
                     ' Всего_Буллиты_назначенные__забитые, Всего_Буллиты_соперник_назначенные__забитые,'
                     ' Всего_Зрители, Всего_Броски_по_воротам, Всего_Броски_по_воротам_соперник,'
                     ' Всего_Реализация_бросков, Всего_Реализация_бросков_соперник, Всего_Вбрасывания,'
                     ' Всего_Выигранные_вбрасывания_проц_от_возможных,'
                     ' Всего_Выигранные_вбрасывания_соперник_проц_от_возможных,'
                     ' Дома_Сыгранные_матчи, Дома_Победы, Дома_Победы_в_овертайме,'
                     ' Дома_Победы_по_буллитам, Дома_Ничьи, Дома_Поражения_по_буллитам,'
                     ' Дома_Поражения_в_овертайме, Дома_Поражения, Дома_Набранные_очки,'
                     ' Дома_Заброшенные_шайбы, Дома_Пропущенные_шайбы, Дома_Разность_шайб,'
                     ' Дома_Штрафное_время, Дома_Буллиты_назначенные__забитые,'
                     ' Дома_Буллиты_соперник_назначенные__забитые, Дома_Зрители,'
                     ' Дома_Броски_по_воротам, Дома_Броски_по_воротам_соперник,'
                     ' Дома_Реализация_бросков, Дома_Реализация_бросков_соперник,'
                     ' Дома_Вбрасывания, Дома_Выигранные_вбрасывания_проц_от_возможных,'
                     ' Дома_Выигранные_вбрасывания_соперник_проц_от_возможных,'
                     ' В_гостях_Сыгранные_матчи, В_гостях_Победы, В_гостях_Победы_в_овертайме,'
                     ' В_гостях_Победы_по_буллитам, В_гостях_Ничьи, В_гостях_Поражения_по_буллитам,'
                     ' В_гостях_Поражения_в_овертайме, В_гостях_Поражения, В_гостях_Набранные_очки,'
                     ' В_гостях_Заброшенные_шайбы, В_гостях_Пропущенные_шайбы, В_гостях_Разность_шайб,'
                     ' В_гостях_Штрафное_время, В_гостях_Буллиты_назначенные__забитые,'
                     ' В_гостях_Буллиты_соперник_назначенные__забитые, В_гостях_Зрители,'
                     ' В_гостях_Броски_по_воротам, В_гостях_Броски_по_воротам_соперник,'
                     ' В_гостях_Реализация_бросков, В_гостях_Реализация_бросков_соперник,'
                     ' В_гостях_Вбрасывания, В_гостях_Выигранные_вбрасывания_проц_от_возможных,'
                     ' В_гостях_Выигранные_вбрасывания_соперник_проц_от_возможных)'
                     )
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS players_stats(Дата, Команда, Номер, Имя, Игры, Заброшеные_шайбы,'
                     ' Заброшенные_шайбы_и_Голевые_передачи, Голевые_передачи, Штрафное_время, '
                     'Пропущеные шайбы)')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS time_table(Дата, Дома, В_гостях, Дома_Голы,'
                     'В_гостях_Голы, Условия_победы)')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS players_stats_2(Команда, Игрок, Амплуа_игрока,'
                     ' Игры, Очки, Голы, Передачи, плюс_минус,'
                     ' Броски_в_створ_ворот, Реализация_бросков_голы_броски, Штрафные_минуты, '
                     'Количество_выходов_на_лед, Время_на_площадке, Отборы_шайбы, Потери_шайбы, '
                     'Силовые_приемы, Блокированные_броски, Выигранные_вбрасывания ,'
                     'Проигранные_вбрасывания,'
                     ' Процент_выигранных_вбрасываний)')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS user_data(id, username, date_reg, date_ban)')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS user_log(id, username, date, command)')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS res_log(Дата, НЗ_Дома, НН_Дома, ЗН_Дома, ЗЗ_Дома, '
                     'В_Дома, СП_Дома, Дома, Дома_Голы, '
                     ' В_гостях_Голы, Условия_победы,'
                     ' В_гостях, НЗ_Гость, НН_Гость, ЗН_Гость, ЗЗ_Гость, В_Гость, СП_Гость)')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS forecast(Дата, Дома, Прогноз_Д, В_гостях, Прогноз_Г)')
        conn.commit()


def set_forecast(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO forecast VALUES(?, ?, ?, ?, ?)', lst)
        conn.commit()


def get_res(date):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        data = cursor.execute(
            'SELECT * FROM res WHERE Дата = "{}"'.format(date)).fetchall()
        return data


def set_res_log(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        date = lst[0][0]
        data = cursor.execute('SELECT * FROM res_log WHERE Дата = "{}"'.format(date)).fetchall()
        if not data:
            for i in lst:
                cursor.execute('INSERT INTO res_log VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', i)
        conn.commit()


def set_user_log(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user_log VALUES(?, ?, ?, ?)', lst)
        conn.commit()


def upd_user_data_on_id(user_id, data):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE user_data SET date_ban="{}" WHERE id = {}'.format(data, user_id))
        conn.commit()


def upd_user_data_on_username(username, data):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE user_data SET date_ban="{}" WHERE username = "{}"'.format(data, username))
        conn.commit()


def set_user_data(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user_data VALUES(?, ?, ?, ?)', lst)
        conn.commit()


def get_user_data(user_id: int):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        data = cursor.execute('SELECT * FROM user_data WHERE id = {}'.format(user_id)).fetchall()
        return data


def set_commands_stats(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO commands_stats VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                       ' ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                       ' ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                       ' ?, ?, ?, ?, ?)', lst)
        conn.commit()


def upd_commands_stats(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE commands_stats SET Дата="{}", Команда="{}", Всего_Сыгранные_матчи="{}",'
                       ' Всего_Победы="{}", Всего_Победы_в_овертайме="{}", Всего_Победы_по_буллитам="{}",'
                       ' Всего_Ничьи="{}", Всего_Поражения_по_буллитам="{}", Всего_Поражения_в_овертайме="{}",'
                       ' Всего_Поражения="{}", Всего_Набранные_очки="{}", Всего_Заброшенные_шайбы="{}",'
                       ' Всего_Пропущенные_шайбы="{}", Всего_Разность_шайб="{}", Всего_Штрафное_время="{}",'
                       ' Всего_Буллиты_назначенные__забитые="{}", Всего_Буллиты_соперник_назначенные__забитые="{}",'
                       ' Всего_Зрители="{}", Всего_Броски_по_воротам="{}", Всего_Броски_по_воротам_соперник="{}",'
                       ' Всего_Реализация_бросков="{}", Всего_Реализация_бросков_соперник="{}",'
                       ' Всего_Вбрасывания="{}", Всего_Выигранные_вбрасывания_проц_от_возможных="{}",'
                       ' Всего_Выигранные_вбрасывания_соперник_проц_от_возможных="{}", Дома_Сыгранные_матчи="{}",'
                       ' Дома_Победы="{}", Дома_Победы_в_овертайме="{}", Дома_Победы_по_буллитам="{}",'
                       ' Дома_Ничьи="{}", Дома_Поражения_по_буллитам="{}", Дома_Поражения_в_овертайме="{}",'
                       ' Дома_Поражения="{}", Дома_Набранные_очки="{}", Дома_Заброшенные_шайбы="{}",'
                       ' Дома_Пропущенные_шайбы="{}", Дома_Разность_шайб="{}", Дома_Штрафное_время="{}",'
                       ' Дома_Буллиты_назначенные__забитые="{}", Дома_Буллиты_соперник_назначенные__забитые="{}",'
                       ' Дома_Зрители="{}", Дома_Броски_по_воротам="{}", Дома_Броски_по_воротам_соперник="{}",'
                       ' Дома_Реализация_бросков="{}", Дома_Реализация_бросков_соперник="{}", Дома_Вбрасывания="{}",'
                       ' Дома_Выигранные_вбрасывания_проц_от_возможных="{}",'
                       ' Дома_Выигранные_вбрасывания_соперник_проц_от_возможных="{}",'
                       ' В_гостях_Сыгранные_матчи="{}", В_гостях_Победы="{}",'
                       ' В_гостях_Победы_в_овертайме="{}", В_гостях_Победы_по_буллитам="{}",'
                       ' В_гостях_Ничьи="{}", В_гостях_Поражения_по_буллитам="{}",'
                       ' В_гостях_Поражения_в_овертайме="{}", В_гостях_Поражения="{}",'
                       ' В_гостях_Набранные_очки="{}", В_гостях_Заброшенные_шайбы="{}",'
                       ' В_гостях_Пропущенные_шайбы="{}", В_гостях_Разность_шайб="{}",'
                       ' В_гостях_Штрафное_время="{}", В_гостях_Буллиты_назначенные__забитые="{}",'
                       ' В_гостях_Буллиты_соперник_назначенные__забитые="{}", В_гостях_Зрители="{}",'
                       ' В_гостях_Броски_по_воротам="{}", В_гостях_Броски_по_воротам_соперник="{}",'
                       ' В_гостях_Реализация_бросков="{}", В_гостях_Реализация_бросков_соперник="{}",'
                       ' В_гостях_Вбрасывания="{}", В_гостях_Выигранные_вбрасывания_проц_от_возможных="{}",'
                       ' В_гостях_Выигранные_вбрасывания_соперник_проц_от_возможных="{}" WHERE Команда="{}"'
                       .format(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8], lst[9], lst[10],
                               lst[11], lst[12], lst[13], lst[14], lst[15], lst[16], lst[17], lst[18], lst[19], lst[20],
                               lst[21], lst[22], lst[23], lst[24], lst[25], lst[26], lst[27], lst[28], lst[29], lst[30],
                               lst[31], lst[32], lst[33], lst[34], lst[35], lst[36], lst[37], lst[38], lst[39], lst[40],
                               lst[41], lst[42], lst[43], lst[44], lst[45], lst[46], lst[47], lst[48], lst[49], lst[50],
                               lst[51], lst[52], lst[53], lst[54], lst[55], lst[56], lst[57], lst[58], lst[59], lst[60],
                               lst[61], lst[62], lst[63], lst[64], lst[65], lst[66], lst[67], lst[68], lst[69], lst[70],
                               lst[1]))
        conn.commit()


def set_players_stats(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO players_stats VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', lst)
        conn.commit()


def upd_player_stat(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        conn.execute('UPDATE players_stats SET Дата="{}", Команда="{}", Номер="{}", Имя="{}", Игры="{}",'
                     ' Заброшеные_шайбы="{}",'
                     ' Заброшенные_шайбы_и_Голевые_передачи="{}",'
                     ' Голевые_передачи="{}", Штрафное_время="{}", '
                     'Пропущеные="{}" WHERE Имя="{}"'.format(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8], lst[9], lst[3]))
        conn.commit()


def set_players_stats_2(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO players_stats_2 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                       ' ?, ?)', lst)
        conn.commit()


def upd_players_stats_2(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        conn.execute('UPDATE players_stats_2 SET Команда="{}", Игрок="{}", Амплуа_игрока="{}",'
                     ' Игры="{}", Очки="{}", Голы="{}", Передачи="{}", плюс_минус="{}",'
                     ' Броски_в_створ_ворот="{}", Реализация_бросков_голы_броски="{}", Штрафные_минуты="{}", '
                     'Количество_выходов_на_лед="{}", Время_на_площадке="{}", Отборы_шайбы="{}", Потери_шайбы="{}", '
                     'Силовые_приемы="{}", Блокированные_броски="{}", Выигранные_вбрасывания="{}" ,'
                     'Проигранные_вбрасывания="{}",'
                     ' Процент_выигранных_вбрасываний="{}" WHERE Игрок="{}"'
                     .format(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8], lst[9], lst[10],
                             lst[11], lst[12], lst[13], lst[14], lst[15], lst[16], lst[17], lst[18], lst[19], lst[1]))
        conn.commit()


def set_time_table(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO time_table VALUES(?, ?, ?, ?, ?, ?)', lst)
        conn.commit()


def upd_time_table(lst):
    with sqlite3.connect(f'bases/data/database.db') as conn:
        conn.execute('UPDATE time_table SET Дата="{}", Дома="{}", В_гостях="{}", Дома_Голы="{}",'
                     'В_гостях_Голы="{}", Условия_победы="{}" WHERE  В_гостях="{}" and Дата=="{}"'.format(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[2], lst[0]))
        conn.commit()


create_table()
