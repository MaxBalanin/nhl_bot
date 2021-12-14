# # -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta
from bases import base

url ='https://nhl.ru/index.php?action=shedul&op=bydateteamseason&stud_season=1&season=24&team1=0&team2=0'


def get_html(url, headers=None, params=None):
    try:
        r = requests.get(url, headers=headers, params=params)
        return r.text
    except Exception as e:
        print('Ошибка реквеста: ', e)


def get_all():
    try:
        soup = BeautifulSoup(get_html(url), 'html.parser')
        table = soup.find_all('form')[2].find_all('table')[1].find_all('tr')[3:]
        all_stat = []
        for i in table:
            match = i.find_all('td')
            data = match[0].string
            if datetime.strptime(data, '%d.%m.%Y') > datetime.strptime(datetime.strftime(datetime.now(), '%d.%m.%Y'), '%d.%m.%Y'):
                break
            elif datetime.strptime(data, '%d.%m.%Y') < datetime.strptime(datetime.strftime(datetime.now(), '%d.%m.%Y'), '%d.%m.%Y'):
                continue
            cm1 = match[1].string
            cm2 = match[2].string
            time = match[3].string
            score = match[5].string + 'r'
            fc = match[6].find('a').get('href')
            fc_url = 'https://nhl.ru/' + fc
            forecast = fc_parser(fc_url)
            summary = [data, cm1, cm2, time, score] + forecast
            all_stat.append(summary)
            print(summary)
        return all_stat
    except Exception as e:
        print('Ошибка реквеста: ', e)


def fc_parser(url):
    try:
        soup = BeautifulSoup(get_html(url), 'html.parser')
        table = soup.find('center').find('table').find_all('tr')[51]
        cm1 = table.find_all('td')[2].string
        cm2 = table.find_all('td')[5].string
        return [int(cm1), int(cm2)]
    except Exception as e:
        print('Ошибка реквеста: ', e)


def save_all():
    tomorrow = datetime.now() + timedelta(days=1)
    for i in get_all():
        w1 = round(i[5] / (i[5] + i[6]) * 100, 1)
        w2 = round(i[6] / (i[5] + i[6]) * 100, 1)
        base.set_forecast([datetime.strftime(tomorrow, '%d.%m.%Y.'), i[1], w1, i[2], w2])
    print('Успешно!')
    return data



