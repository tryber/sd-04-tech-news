import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            resp = []
            file_reader = csv.DictReader(file, delimiter=";")
            for data in file_reader:
                resp.append(data)
            return resp
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
