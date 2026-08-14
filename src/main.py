import requests
from bs4 import BeautifulSoup


url = 'https://www.chitai-gorod.ru/catalog/books'
# columns: title, author, price, status, link

HEADERS = {
   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Sec-Ch-Ua': '"Not;A=Brand";v="99", "Chromium";v="128", "Google Chrome";v="128"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
}


def get_html(url: str):
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)

        if response.status_code == 200:
            HTML = response.text
            return HTML
   
        print(f'Ошибка загрузки страницы. Статус: {response.status_code}')


    except requests.RequestException as error:
        print(f'Возникла сетевая ошибка при запросе к {url}: {error}')
        return None

html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')

book_cards = soup.find('div', class_='product-card__content')

title = book_cards.find('a', class_='product-card__title').text
author = book_cards.find('span', class_='product-card__subtitle').text
price = book_cards.find('span', class_='product-mini-card-price__price product-mini-card-price__price--reverse').text

status = book_cards.find('div', class_='chg-app-button__content').text
if status.lower in ['купить', 'оформить']:
    status = 'В наличии'

link_tag = book_cards.find('a', class_='product-card__title')
link = f"https://www.chitai-gorod.ru{link_tag['href']}" if link_tag else 'Без ссылки'

try:
    print(f'{title} | {author} | {price} | {status} | {link}')
except:
    print('Ошибка.')