import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:

        with open(filepath, encoding="utf-8") as csv_file:
            needed_header = [
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
            header, *data = csv.reader(csv_file, delimiter=";")

            if header != needed_header:
                raise ValueError("Formato invalido")

            return [
                {header[i]: info[i] for i in range(len(info))} for info in data
            ]

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
