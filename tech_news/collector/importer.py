import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            content_reader = csv.DictReader(file, delimiter=";")
            content = ""
            for content in content_reader:
                content_values = content
                return [content_values]
    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
