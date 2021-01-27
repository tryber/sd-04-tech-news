import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    data = find_news()
    if filepath.endswith(".csv"):
        with open(filepath, "w", newline="") as csvfile:
            writer = csv.DictWriter(
                csvfile,
                delimiter=";",
                quotechar='"',
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

            for field in data:
                for key in field:
                    if isinstance(field[key], list):
                        field[key] = ",".join(field[key])

            writer.writeheader()
            writer.writerows(data)
            csvfile.close()
    else:
        raise ValueError("Formato invalido")
