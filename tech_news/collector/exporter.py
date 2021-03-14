import csv
from tech_news.database import find_news

KEYS = [
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


def create_news_list():
    content = find_news()
    for new in content:
        for key in new:
            if isinstance(new[key], list):
                new[key] = ",".join(new[key])
    return content


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    try:
        file = open(filepath, "w")
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        csv_file = csv.DictWriter(file, fieldnames=KEYS, delimiter=";")
        csv_file.writeheader()
        csv_file.writerows(create_news_list())
