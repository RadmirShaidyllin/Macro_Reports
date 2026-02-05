import argparse
import sys
from tabulate import tabulate

from services.csv_loader import load_rows
from reports import REPORTS


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="CSV data with macroeconomic data",
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report name (average-gdp)",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if args.report not in REPORTS:
        print(f"Unknown report: {args.report}")
        sys.exit(1)

    try:
        rows = load_rows(args.files)
    except FileNotFoundError as e:
        print(str(e))
        sys.exit(1)

    report_class = REPORTS[args.report]
    report = report_class()

    result = report.generate(rows)

    indexed = [(i + 1, *row) for i, row in enumerate(result)]

    print(
        tabulate(
            indexed,
            headers=["id", "country", "gdp"],
            tablefmt="grid",
            colalign=("left", "left", "left"),
        )
    )


if __name__ == "__main__":
    main()
