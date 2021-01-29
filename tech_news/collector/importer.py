import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    try:
        with open(filepath, encoding="utf-8") as csv_file:
            exact_format = needed_header = [
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
            csv_reader = csv.DictReader(csv_file, delimiter=";")

            if csv_reader != exact_format:
                raise ValueError("Formato invalido")

            content = ''    
            for content in csv_reader:
                values = [content]
                return values
    
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")

