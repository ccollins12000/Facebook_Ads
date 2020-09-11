import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

def get_page(company_name):
    params = {'q': company_name}
    r = requests.get('http://www.google.com/search', params=params)
    return BeautifulSoup(r.text, 'html.parser')


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


company_list = pd.read_csv('company_list.csv')
all_company_data = []

for company in company_list.loc[:, 'Company']:
    print(company)
    try:
        searched = get_page(company)
        all_company_data.append(pd.DataFrame(data={
            'Searched': [company],
            'Title': [get_gattribute(searched, get_gresult_title)],
            'Address: ': [get_gattribute(searched, get_gresult_address)],
            'Phone: ': [get_gattribute(searched, get_gresult_phone)]
        }))
    except:
        print(company, ' could not be retrieved')

    time.sleep(.5)


all_company_data = pd.concat(all_company_data, axis=0)
all_company_data.to_csv('company_search_results.csv')
