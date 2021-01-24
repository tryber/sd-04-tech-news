import csv


def csv_importer(filepath):

    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    try:
        with open(filepath, encoding="utf-8") as file:
            default = [
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
            header, *data = csv.reader(file, delimiter=";")

            if header != default:
                raise ValueError("Formato invalido")

            return [
                {header[i]: info[i] for i in range(len(info))} for info in data
            ]

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
