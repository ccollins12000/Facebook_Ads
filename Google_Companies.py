import requests
from bs4 import BeautifulSoup

params = {'q': 'Blossom Chevrolet'}
r = requests.get('http://www.google.com/search', params = params)
rtext = BeautifulSoup(r.text, 'html.parser')

print(rtext.findAll('span', {'class': 'BNeawe tAd8D AP7Wnd'}))
print(rtext.findAll('span', {'class': 'BNeawe s3v9rd AP7Wnd'})   )