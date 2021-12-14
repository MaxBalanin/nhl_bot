# # -*- coding: UTF-8 -*-
import json
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


def get_command_link():
    try:
        soup = BeautifulSoup(get_html('https://www.championat.com/hockey/_nhl/tournament/4623/teams/'), 'html.parser')
        all_div = soup.find_all('a', class_="teams-item__link")
        command_list = []
        for i in all_div:
            res = i.get('href').replace('result', 'pstat')
            url = 'https://www.championat.com' + res
            command_list.append(url)
        return command_list
    except Exception as e:
        print('Ошибка реквеста: ', e)


def get_players_stat(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        item = soup.find_all('script', class_='js-table-data-json')[0].string
        name = soup.find_all('div', class_='entity-header__title-name')[0].find('a').string
        players_dict_list = json.loads(item)
        players_list = []
        for player_dict in players_dict_list:
            players_list.append([datetime.strftime(datetime.now(), '%d.%m.%Y.'), name,
                                 player_dict.get('number'), player_dict.get('name'),
                                 player_dict.get('total_game'), player_dict.get('goal'),
                                 player_dict.get('goal_pass'), player_dict.get('pass'),
                                 player_dict.get('penalty'), player_dict.get('minus')])
        print(f'Игроки команды {name} добавлены...')
        return players_list
    except Exception as e:
        print('Ошибка parsing: ', e)


def save_pstats():
    for url in get_command_link():
        for player in get_players_stat(get_html(url)):
            base.set_player_stat(player)
    print('Успешно!')


def upd_pstats():
    for url in get_command_link():
        for player in get_players_stat(get_html(url)):
            base.upd_player_stat(player)
    print('Успешно!')
