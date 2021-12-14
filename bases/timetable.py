# # -*- coding: UTF-8 -*-
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from bases import base

URL = 'https://www.championat.com/hockey/_nhl/tournament/4623/calendar/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/94.0.4606.85 YaBrowser/21.11.0.1999 Yowser/2.5 Safari/537.36',
           'accept': '*/*'}
HOST = 'https://www.championat.com/hockey'


def get_html(params=None):
    r = requests.get(URL, headers=HEADERS, params=params, timeout=10)
    return r.text


def get_timetable():
    try:
        soup = BeautifulSoup(get_html(), 'html.parser')
        item = soup.find_all('td', class_='stat-results__count _order_3')
        timetable = []
        for i in item:
            match = i.find('a').get('title')
            result = i.find('span').string
            tag = i.find_all('span', class_='stat-results__count-ext')
            score = result.split()
            goals = [score[0], score[2]]
            if len(tag) != 0:
                goals.append(tag[0].string)
            date_m = [match.split(',')[1].split(' ')[1]]
            names = match.split(',')[0].split(' - ')
            timetable.append(date_m + names + goals)
            print(f"Матч {match.split(',')[0]} добавлен..")

        return timetable
    except Exception as e:
        print('Ошибка реквеста: ', e)


def save_timetable():
    for battle in get_timetable():
        if len(battle) == 5:
            battle.append('')
        base.set_time_table(battle)
    print('Успешно!')


def upd_timetable():
    for battle in get_timetable():
        if len(battle) == 5:
            battle.append('')
        base.upd_time_table(battle)
    print('Успешно!')