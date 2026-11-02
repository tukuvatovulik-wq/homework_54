# ДЗ №54 — Интернет-магазин

## Запуск проекта

1. Создать виртуальное окружение:
   `py -m venv venv`
2. Активировать его:
   `venv\\Scripts\\activate`
3. Установить Django:
   `pip install -r requirements.txt`
4. Выполнить миграции:
   `py manage.py migrate`
5. Запустить сервер:
   `py manage.py runserver`

Главная страница: http://127.0.0.1:8000/

Редактирование товара: `/products/<id>/edit`

Список категорий: `/categories`

Редактирование категории: `/categories/<id>/edit`
