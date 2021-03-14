import csv
from tech_news.database import find_news

HEAD = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    'sources',
    "categories"
]

def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    resp = find_news()
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        writer = csv.DictWriter(file, fieldnames=HEAD, delimiter=";")

        for item in resp:
            for i in item:
                if isinstance(item[i], list):
                    item[i] = ",".join(item[i])

        writer.writeheader()
        writer.writerows(resp)
        file.close()
