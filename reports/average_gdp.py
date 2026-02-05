from collections import defaultdict
from reports.base import BaseReport


class AverageGDPReport(BaseReport):
    name = "average-gdp"

    def generate(self, rows):
        totals = defaultdict(float)
        counts = defaultdict(int)

        for row in rows:
            country = row["country"]
            gdp = float(row["gdp"])

            totals[country] += gdp
            counts[country] += 1

        result = []

        for country in totals:
            avg = totals[country] / counts[country]
            result.append((country, round(avg, 2)))

        result.sort(key=lambda x: x[1], reverse=True)

        return result
