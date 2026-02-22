# CLI Tool

Консольная утилита для построения отчётов по макроэкономическим данным.

## Требования

- Python 3.12
- Poetry

## Установка

```bash
poetry install
```

## Запуск проекта

```bash
poetry run python main.py --files data/economic1.csv data/economic2.csv --report average-gdp
```

Параметры `--files` и `--report` обязательны.

## Добавление новых данных

Чтобы добавить новые данные:

1. Создайте новый CSV-файл в папке `data/`.
2. Формат файла должен соответствовать существующим примерам:

```
country,year,gdp,gdp_growth,inflation,unemployment,population,continent
```

3. Передайте новый файл через параметр `--files`:

```bash
poetry run python main.py --files data/economic1.csv data/new_data.csv --report average-gdp
```

Отчёт будет построен по всем переданным файлам.