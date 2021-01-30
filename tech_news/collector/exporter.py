import csv
from tech_news.database import find_news

exact_format = [
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

    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(exact_format)
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
