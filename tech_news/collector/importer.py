import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato inválido")
    try:
        with open(filepath) as file:
            content_reader = csv.DictReader(file, delimiter=";")
            content = ""
            for content in content_reader:
                content_values = content
                return [content_values]
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
