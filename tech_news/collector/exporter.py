
from tech_news.database import find_news
import csv


def csv_exporter(filepath):

    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    with open(filepath, "w", newline="", encoding="utf-8") as file:
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

        writer = csv.writer(file, delimiter=";")
        writer.writerow(header)

        for item in news:
            item["sources"] = ",".join(item["sources"])
            item["categories"] = ",".join(item["categories"])
            writer.writerow(list(item.values()))

    csv_exporter("export_correct.csv")
