# import csv

# from ..database import find_news


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato Invalido")
