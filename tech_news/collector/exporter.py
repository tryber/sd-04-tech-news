import csv
from tech_news.database import find_news


def csv_exporter(filepath):

    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    news = find_news()

    for new in news:
        for index in new:
            if isinstance(new[index], list):
                new[index] = ",".join(new[index])

    header = ["url", "title", "timestamp", "writer", "shares_count",
              "comments_count", "summary", "sources", "categories"]

    results = []
    with open(filepath, "w", newline='') as file:
        writer = csv.DictWriter(file, delimiter=";", fieldnames=header)
        writer.writeheader()
        for new in news:
            writer.writerow(new)
            results.append(new)
    file.close()
