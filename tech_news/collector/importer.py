import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    try:
        with open(filepath, encoding="utf-8") as file:
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
            header, *data = csv.reader(file, delimiter=";")

            if header != needed_header:
                raise ValueError("Formato invalido")

            imp_list = [
                {header[i]: info[i] for i in range(len(info))} for info in data
            ]

            return imp_list
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
