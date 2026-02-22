# services/loader.py — загрузка данных из csv

import csv
from typing import Iterable, List, Dict


def load_rows(files: Iterable[str]) -> List[Dict[str, str]]:
    """Читает все файлы и возвращает список словарей."""
    result: List[Dict[str, str]] = []

    for file_path in files:
        try:
            with open(file_path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                result.extend(list(reader))
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")

    return result