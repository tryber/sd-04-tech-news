import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    # Faz a requizição para o banco
    data_news = find_news()

    # Escrita do arquivo
    with open(filepath, "w") as file:
        required_header = [
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
        writer = csv.DictWriter(
            file, fieldnames=required_header, delimiter=";"
        )
        writer.writeheader()

        for row in data_news:
            row["sources"] = ",".join(row["sources"])
            row["categories"] = ",".join(row["categories"])
            writer.writerow(row)


# Teste local
# python3 -i tech_news/collector/exporter.py
# csv_exporter("output.csv")
