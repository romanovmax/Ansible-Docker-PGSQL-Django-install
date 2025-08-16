# Twiclone (Django + Postgres, Docker Compose)

Минимальный «твиттер-клон»: посты (`text` + `image`), лента и пара тестов.

## Быстрый старт

```bash
cp .env.example .env
docker compose up -d
```

Открой: http://localhost:8000

Тесты:
```bash
docker compose exec web python manage.py test
```

## Структура
- `app/` — код Django
- `media/` — загрузки (монтируется внутрь контейнера)
- `docker-compose.yml` — два сервиса: `db` (Postgres) и `web` (Django)

## Настройки БД
Django берёт параметры подключения из `.env`. По умолчанию хост БД — `db` (имя сервиса Compose).
