import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    news = find_news()

    if filepath.endswith(".csv"):
        with open(filepath, "w") as file:
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

            writer = csv.writer(file, delimiter=";")
            writer.writerow(headers)

            new = []

            for key in headers:
                if type(news[0][key]) == list:
                    new.append(",".join(news[0][key]))
                else:
                    new.append(news[0][key])
            print("rows", new)
            writer.writerow(new)

    else:
        raise ValueError("Formato invalido")
