import csv


def converter_object(data, header):
    lista = []
    for row in data:
        item = {}
        for index in range(len(header)):
            item[header[index]] = item[index]
        lista.append(item)

    return lista


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("formato inválido")
    try:
        with open(filepath, "r") as file:
            header_file = [
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

            if header != header_file:
                raise ValueError("formato inválido")

            return converter_object(data, header)

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
