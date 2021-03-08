import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    """exporta do banco de dados para .CSV, delimitando ";" """
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w", newline="", encoding="utf-8") as file:
        filepath_add = csv.DictWriter(
            file, fieldnames=HEADER, delimiter=";"
        )
        new_list = find_news()
        for item in new_list:
            for key in item:
                if type(item[key]) == list:
                    item[key] = ",".join(item[key])

        filepath_add.writeheader()
        filepath_add.writerows(new_list)


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
