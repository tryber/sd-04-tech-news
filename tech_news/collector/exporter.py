import csv
from tech_news import database


def list_to_string(list, separator=""):
    return f"{separator}".join(list)


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
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
        writer.writerow(headers)
        db_result = database.find_news()
        for item in db_result:
            item["sources"] = list_to_string(item["sources"], ",")
            item["categories"] = list_to_string(item["categories"], ",")
            writer.writerow(item.values())
        file.close()
