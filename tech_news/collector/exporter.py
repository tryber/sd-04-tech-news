import csv
from tech_news.database import find_news

FIELD_NAME = [
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


def treating_content_list():
    content = find_news()
    for field in content:
        for key in field:
            if isinstance(field[key], list):
                field[key] = ",".join(field[key])
    return content


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAME, delimiter=";")

        content = treating_content_list()

        writer.writeheader()
        writer.writerows(content)
        