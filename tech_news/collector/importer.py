import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            header, *news = csv.reader(file, delimiter=";")
            expected_header = [
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

            if header != expected_header:
                raise ValueError("Formato inválido")
            formatted_news = [
                {header[i]: article[i] for i in range(len(article))}
                for article in news
            ]
            return formatted_news
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
