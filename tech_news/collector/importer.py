import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            items = ""
            file_content = csv.DictReader(file, delimiter=";")
            for items in file_content:
                content = items
                return [content]
    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
