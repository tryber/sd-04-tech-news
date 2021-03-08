import csv
from tech_news.database import find_news


HEADERS = [
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


def transform_object(news):
    return [
        news["url"],
        news["title"],
        news["timestamp"],
        news["writer"],
        str(news["shares_count"]),
        str(news["comments_count"]),
        news["summary"],
        ",".join(news["sources"]),
        ",".join(news["categories"]),
    ]


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        write_file = csv.writer(file, delimiter=";")
        write_file.writerow(HEADERS)

        for news in find_news():
            write_file.writerow(transform_object(news))
