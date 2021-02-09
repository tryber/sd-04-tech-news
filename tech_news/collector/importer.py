import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    result = []

    try:
        with open(filepath) as file:
            read = csv.DictReader(file, delimiter=";")
            for row in read:
                result.append(row)
            return result

    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
