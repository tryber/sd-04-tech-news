from ..database import find_news
import csv


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        news = find_news()
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
        writer = csv.writer(file)
        writer.writerow(header)
        for row in [[n[h] for n in news] for h in header]:
            writer.writerow(row)
