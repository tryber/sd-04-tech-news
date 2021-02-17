import csv


# https://docs.python.org/pt-br/3/library/csv.html

def csv_importer(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for data_row in reader:
                data = [data_row]
                return data
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
