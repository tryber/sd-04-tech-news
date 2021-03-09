import csv
from tech_news.database import find_news


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


def data_treatment_list():
    data = find_news()
    for field in data:
        for key in field:
            if isinstance(field[key], list):
                field[key] = ",".join(field[key])
    return data


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato inválido")
    with open(filepath, "w") as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=";")

        content = data_treatment_list()

    writer.writeheader()
    writer.writerows(content)
