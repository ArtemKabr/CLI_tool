# main.py — точка входа CLI

import argparse
import sys
from tabulate import tabulate

from services.loader import load_rows
from reports import REPORTS


def parse_args() -> argparse.Namespace:
    """Парсинг аргументов командной строки."""
    parser = argparse.ArgumentParser(description="Macro economic reports")
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to csv files",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report name (e.g. average-gdp)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    report_cls = REPORTS.get(args.report)
    if not report_cls:
        print(f"Unknown report: {args.report}", file=sys.stderr)
        sys.exit(1)

    rows = load_rows(args.files)
    report = report_cls(rows)
    result = report.build()

    formatted = [(country, f"{value:.2f}") for country, value in result]
    print(
        tabulate(
            formatted,
            headers=["country", report.header],
            showindex=True,
            disable_numparse=True,
        )
    )


if __name__ == "__main__":
    main()