import csv


def csv_importer(filepath):
    """retorna erro se nao existir ou se a extensão for invalida"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    """leitura, delimitando e retornando exception caso não exista item"""
    try:
        with open(filepath) as file:
            filepath_teste = csv.DictReader(file, delimiter=";")
            for item in filepath_teste:
                aux = item
                return [aux]
    except FileNotFoundError:
        raise ("Arquivo tests/file_not_exist.csv não encontrado")
