import csv
from tech_news.database import find_news

HEADER = [
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
        csvWriter = csv.DictWriter(file, fieldnames=HEADER, delimiter=";")
        news = find_news()

        for field in news:
            for key in field:
                if type(field[key]) == list:
                    field[key] = ",".join(field[key])

        csvWriter.writeheader()
        csvWriter.writerows(news)
