import os
import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    if not os.path.exists(filepath):
        raise ValueError(f"Arquivo {filepath} não encontrado")

    with open(filepath) as file_csv:
        reader_csv = csv.DictReader(file_csv, delimiter=";", quotechar='"')

        required_header = [
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

        try:
            list_csv = []
            for row in reader_csv:
                element = {}
                for header in required_header:
                    element[header] = row[header]
                list_csv.append(element)
        except KeyError:
            raise ValueError("Formato invalido")

        return list_csv
