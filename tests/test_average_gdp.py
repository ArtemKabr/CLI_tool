from reports.average_gdp import AverageGDPReport


def test_average_gdp_calculation():
    rows = [
        {"country": "A", "gdp": "10"},
        {"country": "A", "gdp": "20"},
        {"country": "B", "gdp": "30"},
    ]

    report = AverageGDPReport(rows)
    result = report.build()

    assert result == [("B", 30.0), ("A", 15.0)]