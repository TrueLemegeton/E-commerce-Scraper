import requests
from bs4 import BeautifulSoup
import time
import random
from openpyxl import Workbook

from pathlib import Path

url = 'https://www.chitai-gorod.ru/catalog/books'
# columns: title, author, price, status, link

HEADERS = {
   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Sec-Ch-Ua': '"Not;A=Brand";v="99", "Chromium";v="128", "Google Chrome";v="128"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"'
}


def get_html(url: str, params=None) -> str:
    '''Делает запрос к странице и возвращает HTML.'''
    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=15)

        if response.status_code == 200:
            HTML = response.text
            return HTML
   
        print(f'Ошибка загрузки страницы. Статус: {response.status_code}')


    except requests.RequestException as error:
        print(f'Возникла сетевая ошибка при запросе к {url}: {error}')
        return None


def parse_books(html: str) -> list[list]:
    '''Собирает необходимые данные со страницы.'''
    soup = BeautifulSoup(html, 'html.parser')

    book_cards = soup.find_all('div', class_='product-card__content')

    book_list = []

    for book in book_cards:
        title_tag = book.find('a', class_='product-card__title')
        title = title_tag.text if title_tag else 'Отсутствует'

        author_tag = book.find('span', class_='product-card__subtitle')
        author = author_tag.text if author_tag else 'Отсутствует'

        price_tag = book.find('span', class_='product-mini-card-price__price product-mini-card-price__price--reverse')
        price = price_tag.text if price_tag else 'Отсутствует'

        status_tag = book.find('div', class_='chg-app-button__content')
        status = status_tag.text.strip() if status_tag else 'Отсутствует'
        if status.lower() in ['купить', 'оформить']:
            status = 'В наличии'
        if status.lower() in ['предзаказ']:
            status = 'Нет в наличии, возможен предзаказ'
        if 'забрать' in status.lower():
            status = 'Забрать из магазина'

        link_tag = book.find('a', class_='product-card__title')
        link = f"https://www.chitai-gorod.ru{link_tag['href']}" if link_tag else 'Без ссылки'

        book_list.append([title,
                          author,
                          price,
                          status,
                          link
        ])

    return book_list


def save_to_excel(books: list[list]):
    """Создает документ .xlsx и сохраняет туда информацию о книгах."""
    wb = Workbook()
    ws = wb.active
    ws.title = 'Книги'

    headers = ['Название', 'Автор', 'Цена', 'Статус', 'Ссылка']
    ws.append(headers)

    for book in books:
        ws.append(book)

    BASE_DIR = Path(__file__).resolve().parent.parent
    output_path = BASE_DIR / 'output' / 'Книги.xlsx'
    wb.save(output_path)

    print('Сохранение прошло успешно!')



def main():
    '''Главный работник программы, выполняет все процессы.'''
    all_books = []

    for page in range(1, 3):
        params = {'page': page}

        html = get_html(url, params)
        books = parse_books(html)
        all_books.extend(books)

        delay = random.uniform(2, 2.5)
        time.sleep(delay)

    save_to_excel(all_books)


if __name__ == '__main__':
    main()