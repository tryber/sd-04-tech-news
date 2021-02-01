import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    data = find_news()

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

            for notice in data:
                for index in notice:
                    if isinstance(notice[index], list):
                        notice[index] = ",".join(notice[index])

            write.writeheader()
            write.writerows(data)
            file.close()

    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
