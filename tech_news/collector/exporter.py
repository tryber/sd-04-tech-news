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

            for new in data:
                for i in new:
                    if isinstance(new[i], list):
                        new[i] = ",".join(new[i])

            writer.writeheader()
            writer.writerows(data)
            csvfile.close()
    else:
        raise ValueError("Formato invalido")
