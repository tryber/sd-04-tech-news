import csv


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    with open(filepath, "w", newline="") as file:
        writer = csv.writer(file)
