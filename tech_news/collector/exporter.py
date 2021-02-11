import csv

from tech_news.database import find_news


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    with open(filepath, "w") as file:
        news = find_news()
        for field in news:
            for key in field:
                if isinstance(field[key], list):
                    field[key] = ",".join(field[key])
        header = [
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

        writer = csv.DictWriter(file, fieldnames=header, delimiter=";")
        writer.writeheader()
        writer.writerows(news)
