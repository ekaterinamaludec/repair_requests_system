# Система учёта заявок на ремонт электрооборудования

## Ссылки на проект

| Где запущено | Ссылка |
|-------------|--------|
| **🌐 Публичный сайт** (PythonAnywhere) | [https://ekaterina123.pythonanywhere.com](https://ekaterina123.pythonanywhere.com) |
| **💻 Локальный запуск** (на своём компьютере) | `http://127.0.0.1:5000` |
| **📁 Репозиторий** (GitHub) | [https://github.com/ekaterinamaludec/repair_requests_system](https://github.com/ekaterinamaludec/repair_requests_system) |

Примечание: если сайт не будет работать (публичный) попробуйте зайти с ВПН.
---

## Описание проекта
Веб-приложение для создания и отслеживания заявок на ремонт электрооборудования.

## Функциональность
- Создание новых заявок
- Просмотр списка всех заявок
- Изменение статуса заявки (Новая → В работе → Выполнена)
- Хранение данных в SQLite базе данных

## Технологии
- Python 3
- Flask
- SQLite
- HTML/CSS

## Установка и запуск (локально)
``bash
1. Клонировать репозиторий:
git clone https://github.com/ekaterinamaludec/repair_requests_system.git
cd repair_requests_system


## 2. Установить зависимости:
pip install flask

## 3. Создать базу данных:
python create_db.py

## 4. Запустить приложение:
python app.py

Открыть в браузере: http://127.0.0.1:5000