import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    with open(filepath, "w") as file:

        headers = [
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

        writer = csv.writer(file, delimiter=";")
        writer.writerow(headers)
        news = find_news()

        for newNews in news:
            writer.writerow(
                [
                    newNews["url"],
                    newNews["title"],
                    newNews["timestamp"],
                    newNews["writer"],
                    newNews["shares_count"],
                    newNews["comments_count"],
                    newNews["summary"],
                    ','.join(newNews["sources"]),
                    ','.join(newNews["categories"]),
                ]
            )