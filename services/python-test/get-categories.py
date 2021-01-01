import requests
from bs4 import BeautifulSoup
import re

url='https://www.citilink.ru/catalog/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

for category in soup.findAll('a', class_="CatalogLayout__item-link", attrs={'href': re.compile("^http(s)?://")}):
    print(category.get('href'))