from reports.average_gdp import AverageGDPReport


def test_average_gdp_basic():
    rows = [
        {"country": "A", "gdp": "10"},
        {"country": "A", "gdp": "20"},
        {"country": "B", "gdp": "5"},
        {"country": "B", "gdp": "15"},
    ]

    report = AverageGDPReport()
    result = report.generate(rows)

    assert result[0][0] == "A"
    assert result[0][1] == 15
    assert result[1][0] == "B"
    assert result[1][1] == 10


def test_sorting_desc():
    rows = [
        {"country": "X", "gdp": "1"},
        {"country": "Y", "gdp": "100"},
    ]

    report = AverageGDPReport()
    result = report.generate(rows)

    assert result[0][0] == "Y"


def test_single_country():
    rows = [
        {"country": "Only", "gdp": "50"},
        {"country": "Only", "gdp": "50"},
    ]

    report = AverageGDPReport()
    result = report.generate(rows)

    assert result == [("Only", 50.0)]
