# reports/__init__.py — реестр отчётов

from reports.average_gdp import AverageGDPReport

REPORTS = {
    "average-gdp": AverageGDPReport,
}