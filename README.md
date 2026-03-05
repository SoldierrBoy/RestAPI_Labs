# Library REST API

REST API для керування бібліотекою, реалізований за допомогою FastAPI.

## Функціонал

* Створення книги
* Отримання списку книг
* Отримання книги за ID
* Видалення книги
* Limit-Offset пагінація

## Технології

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Docker
* Docker Compose
* Pytest

## Запуск проекту

### 1. Клонувати репозиторій

git clone <https://github.com/SoldierrBoy/RestAPI_Labs>
cd RestAPI_Labs

### 2. Запустити Docker

docker compose up --build

API буде доступне за адресою:

http://localhost:8000

Swagger документація:

http://localhost:8000/docs

## Тести

Запуск тестів:

pytest

## Приклад пагінації

GET /books?limit=2&offset=0

GET /books?limit=2&offset=2
