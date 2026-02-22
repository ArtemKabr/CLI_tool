# reports/average_gdp.py — отчёт среднего ВВП

from collections import defaultdict
from typing import List, Dict, Tuple

from reports.base import BaseReport


class AverageGDPReport(BaseReport):
    """Отчёт: средний ВВП по странам."""

    header = "gdp"

    def build(self) -> List[Tuple[str, float]]:
        grouped = defaultdict(list)

        for row in self.rows:
            country = row["country"]
            gdp = float(row["gdp"])
            grouped[country].append(gdp)

        result = []
        for country, values in grouped.items():
            avg = sum(values) / len(values)
            result.append((country, round(avg, 2)))

        result.sort(key=lambda x: x[1], reverse=True)
        return result