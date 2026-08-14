# E-commerce Scraper

## Description

Парсер собирает название, автора, цену, статус товара и ссылку на товар с сайта [Читай-город](https://www.chitai-gorod.ru/catalog/books).

## Features

- Сбор названия книги
- Сбор автора
- Сбор цены
- Сбор статуса товара
- Сбор ссылки на товар

## Technologies

- Python
- Requests
- BeautifulSoup

## Installation

1. Клонировать репозиторий

```bash
git clone https://github.com/TrueLemegeton/E-commerce-Scraper
```

2. Перейти в папку проекта

```bash
cd E-commerce-Scraper
```

3. Создать виртуальное окружение

```bash
python -m venv .venv
```

4. Активировать виртуальное окружение

```bash
./.venv/Scripts/Activate
```

5. Установить зависимости

```bash
pip install -r requirements.txt
```

## Usage

Запустите парсер из корневой директории проекта:

```bash
python src/main.py
```

## Output

Сейчас данные выводятся в консоль в формате:

```text
Если все кошки в мире исчезнут (покет) | Гэнки Кавамура | 389 ₽ |  Купить | https://www.chitai-gorod.ru/product/esli-vse-koshki-v-mire-ischeznut-poket-2968841
```


## Project Structure

```text
e-commerce-scraper/
├── src/
│   └── main.py
├── .gitignore
├── README.md
└── requirements.txt
```
