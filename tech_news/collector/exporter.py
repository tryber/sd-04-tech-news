import csv
from tech_news.database import find_news


FIELD_HEADER = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    "sources",
    "categories",
]


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w", newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_HEADER, delimiter=";")

        header = find_news()
        for field in header:
            for key in field:
                if type(field[key]) == list:
                    field[key] = ",".join(field[key])

        writer.writeheader()
        writer.writerows(header)
