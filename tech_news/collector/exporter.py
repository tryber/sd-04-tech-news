import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
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
        writer.writerow(headers)

        news = find_news()

        for row in news:
            writer.writerow([
                row["url"],
                row["title"],
                row["timestamp"],
                row["writer"],
                row["shares_count"],
                row["comments_count"],
                row["summary"],
                ','.join(row["sources"]),
                ','.join(row["categories"]),
                ])
