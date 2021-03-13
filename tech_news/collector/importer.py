import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            filepath_teste = csv.DictReader(file, delimiter=";")
            for item in filepath_teste:
                aux = item
                return [aux]
    except FileNotFoundError:
        raise ValueError("Arquivo {filepath} não encontrado")
