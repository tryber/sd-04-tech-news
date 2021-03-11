import csv


def csv_importer(filepath):
    print(filepath)
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    try:
        results = []
        with open(filepath, encoding="utf-8") as file:
            news_reader = csv.DictReader(file, delimiter=";")
            print(news_reader.fieldnames)
            for row in news_reader:
                results.append(row)
            return results
    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
