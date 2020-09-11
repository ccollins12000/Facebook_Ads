import requests
import pandas as pd
from bs4 import BeautifulSoup

searched = 'Blossom Chevrolet'

params = {'q': searched}
r = requests.get('http://www.google.com/search', params=params)
r_html = BeautifulSoup(r.text, 'html.parser')


def get_gresult_title(bs4_html):
    return (bs4_html.find('div', {'id': 'main'}).find('div', {'class': 'ZINbbc xpd O9g5cc uUPGi'}).find('h3', {
        'class': "zBAuLc"}).text)


def get_gresult_address(bs4_html):
    for el in bs4_html.find('div', {'id': 'main'}).find('div', {'class': 'ZINbbc xpd O9g5cc uUPGi'}).findAll('div', {
        'class': 'BNeawe s3v9rd AP7Wnd'}):
        txt = el.text
        if txt.find('Address: ') == 0:
            return (txt.replace('Address: ', ''))


def get_gresult_phone(bs4_html):
    for el in r_html.find('div', {'id': 'main'}).find('div', {'class': 'ZINbbc xpd O9g5cc uUPGi'}).findAll('div', {
        'class': 'BNeawe s3v9rd AP7Wnd'}):
        txt = el.text
        if txt.find('Phone: ') == 0:
            return txt.replace('Phone: ', '')


def get_gattribute(bs4_html, fun):
    try:
        return fun(bs4_html)
    except:
        print(searched, ' Attribute Not Found')
        return ''


print(pd.DataFrame(data={
    'Searched': [searched],
    'Title': [get_gresult_title(r_html)],
    'Address: ': [get_gresult_address(r_html)],
    'Phone: ': [get_gresult_phone(r_html)]
}))
