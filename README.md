# VPa03

Простое приложение для скачивания страницы по URL.

## Установка

```bash
python -m venv .venv
source .venv/bin/activate
pip install requests
```

## Запуск

```bash
python main.py https://example.com
```

Если URL не указан, используется значение по умолчанию `https://something.com`.

## Тесты

```bash
python -m unittest test_main -v
```

## Структура

- `main.py` — точка входа: `fetch(url)` выполняет запрос, `main()` разбирает аргументы и печатает результат
- `test_main.py` — тесты на `unittest`