import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        csv_file = open(filepath)
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        csv_content = csv.DictReader(csv_file, delimiter=";")
        return [content for content in csv_content]
