import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    file = open(filepath, "w")
    csv_writer = csv.writer(file, delimiter=";")
    news = find_news()
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
    csv_writer.writerow(headers)
    for new in news:
        new["sources"] = ','.join(new["sources"])
        new["categories"] = ','.join(new["categories"])
        print(new.values())
        csv_writer.writerow(new.values())
    file.close()
