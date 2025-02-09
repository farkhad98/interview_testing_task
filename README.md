# 🚀 FastAPI + Docker + Alembic

## 📌 Описание
Этот проект представляет собой REST API для справочника организаций, зданий и их деятельности. В проекте используется **FastAPI**, **PostgreSQL**, **Alembic** для миграций и разворачивается с помощью **Docker Compose**.

## 🛠 Требования
Перед запуском убедитесь, что у вас установлены:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Make](https://www.gnu.org/software/make/)

## 🚀 Запуск проекта

### 1️⃣ Собрать и запустить контейнеры
```sh
make build  # Собираем контейнеры
make up     # Запускаем проект
```

### 2️⃣ Вход в контейнер с веб-приложением
```sh
make enter_web
```

### 3️⃣ Применить миграции базы данных
```sh
alembic upgrade head
```

### 4️⃣ Открыть документацию API
После запуска проекта документация будет доступна по адресу:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)

После запуска проекта заполните базу данных по ссылке:
- **Swagger UI**: [http://localhost:8000/docs#/default/root__get](http://localhost:8000/docs#/default/root__get)

Пример запроса для получения организаций в заданном квардрате, все параметры обязательны:

- Координаты левого верхнего угла прямоугольника:
    - left_top_coordinates_x
    - left_top_coordinates_y

- Координаты правого верхнего угла прямоугольника:
    - right_top_coordinates_x
    - right_top_coordinates_y

- Координаты правого нижнего угла прямоугольника:
    - right_bottom_coordinates_x
    - right_bottom_coordinates_y

- Координаты левого нижнего угла прямоугольника:
    - left_bottom_coordinates_x
    - left_bottom_coordinates_y

Координаты должны окружать определнный периметр в соответствии с координатной плоскостью локации, то есть, искомое будет правее левого ребра и левее правого по координатной сетке. Так же и для оси Y.

## 🛠 Основные команды

| Команда | Описание |
|---------|------------|
| `make build` | Собрать контейнеры |
| `make up` | Запустить контейнеры |
| `make down` | Остановить контейнеры |
| `make restart` | Перезапустить контейнеры |
| `make enter_web` | Войти в контейнер веб-приложения |
| `make logs` | Просмотр логов |

## 🔥 Дополнительно
- **База данных**: PostgreSQL
- **Миграции**: Alembic
- **Документация API**: OpenAPI (Swagger)

