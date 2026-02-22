# reports/base.py — базовый класс отчёта

from abc import ABC, abstractmethod
from typing import List, Dict, Tuple


class BaseReport(ABC):
    """Базовый класс для всех отчётов."""

    header: str

    def __init__(self, rows: List[Dict[str, str]]):
        self.rows = rows

    @abstractmethod
    def build(self) -> List[Tuple[str, float]]:
        """Формирует данные для вывода."""
        pass