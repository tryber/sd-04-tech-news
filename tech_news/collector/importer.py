import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            filepath_reader = csv.DictReader(file, delimiter=";")
            for item in filepath_reader:
                values = item
                return [values]
    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")