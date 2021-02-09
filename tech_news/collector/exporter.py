import csv
from tech_news.database import find_news

HEADERS = [
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

# transformando shares e comments para string


def transform_object(news):
    return [
        news["url"],
        news["title"],
        news["timestamp"],
        news["writer"],
        str(news["shares_count"]),
        str(news["comments_count"]),
        news["summary"],
        # separar por virgula os elementos
        ",".join(news["sources"]),
        # separar por virgula os elementos
        ",".join(news["categories"]),
    ]


# Join PYTHON => https://www.w3schools.com/python/ref_string_join.asp
#  myTuple = ("John", "Peter", "Vicky")
#  x = "#".join(myTuple)
#


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        write_file = csv.writer(file, delimiter=";")
        write_file.writerow(HEADERS)

        for news in find_news():
            write_file.writerow(transform_object(news))
