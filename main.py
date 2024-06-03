import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

file = open('read.txt', 'w', encoding="utf-8")

link_channel = requests.get(input('link: '))  # https://t.me/s/...
html = bs(link_channel.text, 'html.parser')

massages = html.find_all('div', class_='tgme_widget_message_text js-message_text')
times = html.find_all('time', class_='time')
pprint(massages)


def tg_times():
    for time in times:
        x = str(time.text)
        return x


for massage in massages:
    file.write(str(massage.text) + ';' + str(tg_times()) + '\n')

file.close()
