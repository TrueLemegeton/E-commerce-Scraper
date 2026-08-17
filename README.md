# E-commerce Scraper

## Description

Парсер собирает название, автора, цену, статус товара и ссылку на товар с сайта [Читай-город](https://www.chitai-gorod.ru/catalog/books).

## Features

- Сбор названия книги
- Сбор автора
- Сбор цены
- Сбор статуса товара
- Сбор ссылки на товар
- Парсинг нескольких страниц каталога
- Задержка между запросами
- Cохранение в XLSX

## Technologies

- Python
- Requests
- BeautifulSoup
- openpyxl

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

После запуска файл сохраняется в:

```text
output/Книги.xlsx
```


## Project Structure

```text
e-commerce-scraper/
├── src/
│   └── main.py
├── output/
├── .gitignore
├── README.md
└── requirements.txt
```
