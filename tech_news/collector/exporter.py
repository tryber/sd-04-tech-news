import csv
from tech_news.database import find_news

FIELDNAMES = [
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


def join_list():
    content = find_news()
    for field in content:
        for key in field:
            if isinstance(field[key], list):
                field[key] = ",".join(field[key])
    return content


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        file = open(filepath, "w")
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        writed_file = csv.DictWriter(
            file, fieldnames=FIELDNAMES, delimiter=";"
        )
        writed_file.writeheader()
        writed_file.writerows(join_list())
