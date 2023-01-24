"""  
1) Получить html код страницы
2) Получить карточки товаров
3) Распарсить данные из карточки
4) Записать данные в файл
"""
import csv

import requests # для отправки запросов - получения html кода
from bs4 import BeautifulSoup # для фильтрации html-кода
from bs4.element import ResultSet, Tag # для аннотации типов

URL = 'https://www.kivano.kg/noutbuki' # ссылка на сайт, который будем парсить

response = requests.get(URL) # отправляем запрос на сайт и получаем ответ 

html = response.text # из ответа полученного с сайта получаем html-код с помощью .text

soup = BeautifulSoup(html, 'html.parser') # с помощью BeautifulSoup получаем доступ ко всем тегам html-кода (создаем суп страницы)

cards = soup.find_all('div', class_='item') # из супа находим ВСЕ теги с именем div, но так как div на сайте очень много, достаем конкретно нужные нам, указав их класс 'item', с помощью .find_all()

result = [] # создали пустой список, чтобы сохранять в него конечный результат
for tag in cards: # проходимся циклом по списку тегов
    title = tag.find('div', class_='listbox_title oh').text # обращаемся к каждому тегу внутри списка и достаем от туда название с помощью .find() 
    price = tag.find('div', class_='listbox_price').text # достаем цену
    desc = tag.find('div', class_='product_text').text # достаем описание
    img_link = tag.find('div', class_='listbox_img').find('img').get('src') # достаем ссылку на картинку, которая находится в атрибуте тега img. Чтобы обращаться к атрибутам тега используется метод .get()
    
    obj = { # создаем словарь, который представляет собой каждый товар, который мы достали с сайта
        'title': title.strip(), 
        'price': price.strip(),
        'description': desc.strip().replace('\n', ''),
        'image_link': img_link,
    }
    result.append(obj) # добавляем каждый словарик в список


with open('notebooks.csv', 'w') as file: # открываем файл, чтобы записать в него данные из словарей
    names = ['title', 'price', 'description', 'image_link'] # в список сохраняем названия столбцов таблицы. Названия должны совпадать с именами ключей в словаре obj
    writer = csv.DictWriter(file, fieldnames=names) # создаем специальный тип данных, который служит для записи словарей в таблицы. В fieldnames указываем названия столбцов.
    writer.writeheader() # записываем названия столбцов, взятые из fieldnames
    for notebook in result: # проходимся циклом по списку со словарями
        writer.writerow(notebook) # с помощью .writerow() записываем каждый словарь в таблицу


