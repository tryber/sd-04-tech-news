import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    try:
        with open(filepath) as file:
            reader = csv.reader(file, delimiter=";")
            return reader
    except FileNotFoundError:
        raise ValueError("Arquivo {filepath} não encontrado")
    else:
        file.close()
