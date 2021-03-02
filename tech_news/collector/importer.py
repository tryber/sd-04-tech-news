import csv
# from pprint import pprint


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    try:
        with open(filepath) as file:
            reader = csv.DictReader(file, delimiter=";")
            # result = []
            for row in reader:
                reader = [row]
                # print("Vai imprimir aqui xxxxxxxxxxxxxxxxxxxxx", row)
            return reader
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        file.close()
