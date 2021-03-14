import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    data = find_news()
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        file_writer = csv.DictWriter(file, delimiter=";", fieldnames=[
            "url",
            "title",
            "timestamp",
            "writer",
            "shares_count",
            "comments_count",
            "summary",
            "sources",
            "categories",
        ])

        for item in data:
            for indice in item:
                if isinstance(item[indice], list):
                    item[indice] = ",".join(item[indice])

        file_writer.writeheader()
        file_writer.writerows(data)
        file.close()
