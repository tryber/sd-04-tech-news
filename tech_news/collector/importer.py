import csv


# Funções auxiliares para fazer o csv_importer
def make_csv_list(reader_csv, required_header):
    list_csv = []
    for row in reader_csv:
        element = {}
        for header in required_header:
            element[header] = row[header]
        list_csv.append(element)
    return list_csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    try:
        with open(filepath) as file_csv:
            reader_csv = csv.DictReader(file_csv, delimiter=";", quotechar='"')

            required_header = [
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

            list_csv = make_csv_list(reader_csv, required_header)

    except KeyError:
        raise ValueError("Formato invalido")
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")

    return list_csv
