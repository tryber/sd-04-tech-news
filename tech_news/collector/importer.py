import csv


def csv_importer(filepath):
    try:
        if not filepath.endswith(".csv"):
            raise ValueError("Formato invalido")
        with open(filepath) as file:
            news_reader = csv.DictReader(file, delimiter=";")
            DICT = list(news_reader)
    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
    else:
        return DICT
