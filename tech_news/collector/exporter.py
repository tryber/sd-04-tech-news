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
    with open(filepath, "w", newline="", encoding="utf-8") as file:
        filepath_writer = csv.DictWriter(
            file, fieldnames=HEADER, delimiter=";"
        )
        list_news = find_news()
        for item in list_news:
            for key in item:
                if type(item[key]) == list:
                    item[key] = ",".join(item[key])

        filepath_writer.writeheader()
        filepath_writer.writerows(list_news)