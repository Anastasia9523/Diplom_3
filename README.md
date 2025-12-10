# UI Автотесты для сервиса Stellar Burgers  
Дипломный проект №3 — автоматизация тестирования веб-приложения бургерной Stellar Burgers  
(https://stellarburgers.education-services.ru)

## Описание проекта

Репозиторий содержит набор автоматизированных UI-тестов для проверки ключевых пользовательских сценариев веб-приложения Stellar Burgers.  
Тесты написаны на **Python + Pytest + Selenium WebDriver**, структура построена по принципам **Page Object Model (POM)**.

Тесты покрывают:
- функциональность конструктора бургеров  
- модальные окна ингредиентов  
- создание заказа  
- обновление и корректность статистики заказов в ленте  
- авторизацию пользователя  


## Используемые технологии

- **Python 3.10+**
- **Pytest**
- **Selenium WebDriver**
- **webdriver-manager** (для автозагрузки драйверов)
- **Allure** (шаги, красивые отчёты)
- **Page Object Model (POM)**

## Структура проекта

Diplom_3/
│
├── tests/
│ ├── test_constructor.py
│ └── test_order_feed.py 
│
├── pages/
│ ├── base_page.py
│ ├── main_page.py
│ ├── modal_page.py
│ ├── login_page.py
│ └── order_feed_page.py
│
├── locators/
│ ├── main_page_locators.py
│ ├── modal_locators.py
│ ├── order_feed_locators.py
│ └── login_locators.py
│
├── data/
│ ├── urls.py
│ └── user.py
│
├── conftest.py 
└── README.md

## Запуск всех тестов
pytest

## Запуск конкретного файла
pytest tests/test_order_feed.py

## Запуск с выводом шагов Allure
pytest --alluredir=allure-results
allure serve allure-results