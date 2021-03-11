import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        csv_file = open(filepath)
    except FileNotFoundError:
        return  ValueError(f"Arquivo {filepath} não encontrado")
    else:
        read_content = csv.DictReader(csv_file, delimiter=";")
        for content in read_content:
            values = content
            return [values]
