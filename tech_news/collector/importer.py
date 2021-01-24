import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""

    with open("balneabilidade.csv") as file:
        news = csv.reader(file, delimiter=";")
        header, *data = news
