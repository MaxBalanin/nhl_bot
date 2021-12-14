# # -*- coding: UTF-8 -*-
import os
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from bases import base

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/94.0.4606.85 YaBrowser/21.11.0.1999 Yowser/2.5 Safari/537.36',
           'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params, timeout=10)
    return r.text


def get_title():
    try:
        soup = BeautifulSoup(get_html('https://www.championat.com/hockey/_nhl/tournament/4623/teams/223443/tstat/'),
                             'html.parser')
        main_head = soup.find_all('th', class_='_center _group-head _hidden-td')
        main_list = []
        for i in main_head:
            main_list.append(i.string)
        s_list = []
        s_head = soup.find_all('td', class_='_big')
        result = ['Дата', 'Команда']
        for i in s_head:
            s_list.append(i.string)
        for m in main_list:
            for s in s_list:
                result.append(f'{m}: {s}')
        return result
    except Exception as e:
        print('Ошибка реквеста: ', e)


def get_update(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        all_head = soup.find_all('td', class_='_center _group-start _group-end')
        all_list = []
        for i in all_head:
            all_list.append(i.string)

        temp_head = soup.find_all('td', class_='_center _group-start _group-end _hidden-td')
        temp_list = []
        home_list = []
        out_list = []
        for i in temp_head:
            temp_list.append(i.string)
        for g in range(len(temp_list)):
            if g % 2 == 0:
                home_list.append(temp_list[g])
            else:
                out_list.append((temp_list[g]))
        return all_list, home_list, out_list
    except Exception as e:
        print('Ошибка реквеста: ', e)


def get_command_link():
    try:
        soup = BeautifulSoup(get_html('https://www.championat.com/hockey/_nhl/tournament/4623/teams/'), 'html.parser')
        all_div = soup.find_all('a', class_="teams-item__link")
        command_list = []
        for i in all_div:
            res = i.get('href').replace('result', 'tstat')
            url = 'https://www.championat.com' + res
            command_list.append(url)
        return command_list
    except Exception as e:
        print('Ошибка реквеста: ', e)


def get_content(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        update = get_update(html)
        item = soup.find_all('table', class_='table table-stripe _indent-top')
        name = soup.find_all('div', class_='entity-header__title-name')[0].find('a').string
        alls = [datetime.strftime(datetime.now(), '%Y-%m-%d.'), name, update[0][0]]
        temp = []
        home = [update[1][0]]
        out = [update[2][0]]
        all_match = item[0].findAll('td', class_='_center _group-start')
        for i in all_match:
            alls.append(i.string)
        home_out_match = item[0].findAll('td', class_='_center _group-start _hidden-td')
        for i in home_out_match:
            temp.append(i.string)
        for g in range(len(temp)):
            if g % 2 == 0:
                home.append(temp[g])
            else:
                out.append(temp[g])
        alls[-4], alls[-5] = alls[-4] + ' r', alls[-5] + ' r'
        home[-4], home[-5] = home[-4] + ' r', home[-5] + ' r'
        out[-4], out[-5] = out[-4] + ' r', out[-5] + ' r'
        alls += (update[0][1:])
        home += (update[1][1:])
        out += (update[2][1:])
        print(f'Команда {name} добавлена...')
        res = alls + home + out
        return res
    except Exception as e:
        print('Ошибка реквеста: ', e)


def save_commands_stats():
    for url in get_command_link():
        base.set_commands_stats(get_content(get_html(url)))
    print('Успешно!')


def upd_commands_stats():
    for url in get_command_link():
        base.upd_commands_stats(get_content(get_html(url)))
    print('Успешно!')

