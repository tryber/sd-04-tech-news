import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    try:
        with open(filepath, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            content = ""
            for content in reader:
                values = [content]

                return values

    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
