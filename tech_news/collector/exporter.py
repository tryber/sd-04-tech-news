import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    # print(find_news())
    try:
        if not filepath.endswith(".csv"):
            # https://docs.python.org/3/tutorial/errors.html (8.4)
            raise ValueError("Formato invalido")
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
        # https://docs.python.org/pt-br/3/library/csv.html#csv.csvwriter.writerow
        writer.writerow(headers)
        noticias = find_news()

        for noticia in noticias:
            writer.writerow(
                [
                    noticia["url"],
                    noticia["title"],
                    noticia["timestamp"],
                    noticia["writer"],
                    noticia["shares_count"],
                    noticia["comments_count"],
                    noticia["summary"],
                    ','.join(noticia["sources"]),
                    ','.join(noticia["categories"]),
                ]
            )

    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
