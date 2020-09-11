import requests
import BeautifulSoup from bs4

params = {'q': 'Bill McRae Ford Lincoln'}
r = requests.get('http://www.google.com/search', params = params)
rtext = BeautifulSoup(r.text, 'html.parser')

rtext.findAll('span', {'class': 'BNeawe tAd8D AP7Wnd'})
rtext.findAll('span', {'class': 'BNeawe s3v9rd AP7Wnd'})    