import sqlite3
from bs4 import BeautifulSoup
import requests

def parsing_sulpak_smartfoniy():
    url = 'https://www.sulpak.kg/osh'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    name_product = soup.find_all('div', class_='product__item-name')
    price_product = soup.find_all('div', class_='product__item-price')

    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    for name, price in zip(name_product, price_product):
        name_text = name.find('a').text.strip()
        price_text = price.text.strip().replace('сом', '').replace(',', '')

        cursor.execute("INSERT INTO posts_product (name, price) VALUES (?, ?);", (name_text, price_text))

    connection.commit()
    connection.close()



parsing_sulpak_smartfoniy()