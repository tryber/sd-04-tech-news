from ..database import find_news
import csv

def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w", newline="", encoding='utf-8') as file:
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
        for n in news:
            n["sources"] = ','.join(n["sources"])
            n["categories"] = ','.join(n["categories"])
            writer.writerow(list(n.values()))


csv_exporter("export_correct.csv")
