import csv

def csv_importer(filepath):
    try:
        if not filepath.endswith(".csv"):
            raise ValueError("Formato invalido")
        with open(filepath) as file:
            data_reader = csv.reader(file, delimiter=";")
            headers = [
                    "url",
                    "title",
                    "timestamp",
                    "writer",
                    "shares_count",
                    "comments_count",
                    "summary",
                    "sources",
                    "categories",
                ]
            header, *data = data_reader
            if header != headers:
                raise ValueError("Formato invalido")
            result = [{header: data for header, data in zip(header, data)} for data in data]
            return result
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
