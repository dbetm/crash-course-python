import urllib.request
from bs4 import BeautifulSoup

datos = urllib.request.urlopen('https://www.openwebinars.net').read().decode()

soup = BeautifulSoup(datos, 'lxml')
tags = soup('a')

for tag in tags:
    print(tag.get('href'))
