# # -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import csv
from datetime import datetime
from bs4 import BeautifulSoup
from bases import base

url = 'http://nhl.ru/index.php'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/94.0.4606.85 YaBrowser/21.11.0.1999 Yowser/2.5 Safari/537.36',
           'accept': '*/*'}

def get_list():
    driver = webdriver.Chrome(executable_path=f'bases/chrome_driver/chromedriver.exe')

    try:
        driver.get(url=url)
        time.sleep(2)
        login = driver.find_elements(By.NAME, 'username')
        login[0].send_keys('')
        time.sleep(2)
        pas = driver.find_elements(By.NAME, 'password')
        pas[0].send_keys('')
        pas[0].send_keys(Keys.ENTER)
        time.sleep(3)
        driver.get(url='http://nhl.ru/index.php?action=statistic')
        time.sleep(4)
        with open('bases/pages/page1.html', 'w') as f:
            f.write(driver.page_source)
        for i in range(2, 17):
            pages_list = driver.find_element(By.CLASS_NAME, 'navigation')
            pages_list.find_element(By.LINK_TEXT, f'{i}').click()
            time.sleep(4)
            phtml = driver.page_source
            with open(f'bases/pages/page{i}.html', 'w') as f:
                f.write(phtml)
            time.sleep(2)
    except Exception as e:
        print('Ошибка selenium: ', e)
    finally:
        driver.close()
        driver.quit()


def get_soups(i):
    with open(f'bases/pages/page{i}.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        return soup


headers_list = ['Команда', 'Игрок', 'Амплуа игрока', 'Игры', 'Очки', 'Голы', 'Передачи', '+/-', 'Броски в створ ворот',
                'Реализация бросков (голы/броски)', 'Штрафные минуты', 'Количество выходов на лед', 'Время на площадке',
                'Отборы шайбы', 'Потери шайбы', 'Силовые приемы', 'Блокированные броски', 'Выигранные вбрасывания',
                'Проигранные вбрасывания', 'Процент выигранных вбрасываний']


def parse(soup: BeautifulSoup):
    try:
        table = soup.find('table', class_='rtable').find_all('tr')
        pl_list = []
        for j in range(1, len(table), 2):
            pl_info = []
            pl = table[j]
            cm = pl.find('img').get('title')
            pl_info.append(cm)
            nm = pl.find_all('a')[1].string
            pl_info.append(nm)
            bl = pl.find_all('td')
            for i in range(5, len(bl)):
                pl_info.append(bl[i].string)
            pl_list.append(pl_info)
            print(f'Игрок {nm} добавлен...')
        return pl_list
    except Exception as e:
        print('Ошибка parsig: ', e)


def save_pstats2():
    for i in range(1, 17):
        pl_lt = parse(get_soups(i))
        for pl in pl_lt:
            base.set_players_stats_2(pl)
    print('Успешно!')


def upd_pstats2():
    for i in range(1, 17):
        pl_lt = parse(get_soups(i))
        for pl in pl_lt:
            base.upd_players_stats_2(pl)
    print('Успешно!')

