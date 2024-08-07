# README

## Описание

Это тестовое задание представляет собой API, которое позволяет получать новости за заданный период из базы данных
и парсер, который каждые 10 минут парсит новости с сайта [mosday.ru](http://mosday.ru/news/tags.php?metro). При первой загрузке парсер получает все доступные новости и сохраняет их в базе данных с меткой времени.

## Установка

### Требования

- Python 3.10+
- Docker
- Docker Compose

### Запуск приложения

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/zakhep66/metro_test-task.git
   cd metro_test-task
   ```

2. Переименуйте и заполните файл .env-example в .env

3. Запустите приложение:
   ```bash
   make app
   ```
4. Выполните миграции базы данных:
   ```bash
   make app-migrations
   make app-migrate
   ```