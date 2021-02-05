# import csv

# from ..database import find_news


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato Invalido")
    try:
        with open(filepath, "w") as file:
            print(file)
            writer = file.write('teste')
            print(writer)

    except FileNotFoundError:
        raise ValueError("Formato Invalido")
