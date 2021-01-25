import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as csv_file:
        data = find_news()
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(csv_file, fieldnames, delimiter=";")
        writer.writeheader()
        for obj in data:
            obj["sources"] = ",".join(obj["sources"])
            obj["categories"] = ",".join(obj["categories"])
            writer.writerows(data)
        csv_file.close()
