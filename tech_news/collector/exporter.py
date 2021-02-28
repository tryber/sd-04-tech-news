import csv
from tech_news.database import find_news

header = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "summary",
    "sources",
    "categories",
]


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        whriteCsv = csv.DictWriter(file, fieldnames=header, delimiter=";")
        findNews = find_news()
        for field in findNews:
            for key in field:
                if type(field[key]) == list:
                    field[key] = ",".join(field[key])

        whriteCsv.writeheader()
        whriteCsv.writerows(findNews)
