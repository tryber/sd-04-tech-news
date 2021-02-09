import csv
from tech_news.database import find_news


def content_notices():
    data = find_news()
    for notice in data:
        for index in notice:
            if isinstance(notice[index], list):
                notice[index] = ",".join(notice[index])
    return data


def csv_exporter(filepath):

    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    try:
        with open(filepath, "w") as file:
            write = csv.DictWriter(
                file,
                delimiter=";",
                fieldnames=[
                    "url",
                    "title",
                    "timestamp",
                    "writer",
                    "shares_count",
                    "comments_count",
                    "summary",
                    "sources",
                    "categories",
                ],
            )
            content = content_notices()

            write.writeheader()
            write.writerows(content)
            file.close()

    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
