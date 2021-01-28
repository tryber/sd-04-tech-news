from pathlib import Path
import csv


def csv_importer(filepath):
    if filepath.endswith(".csv"):
        if Path(filepath).is_file():
            results = []
            with open(filepath) as file:
                csv_reader = csv.DictReader(file, delimiter=";", quotechar='"')
                for row in csv_reader:
                    results.append(row)
                return results

        else:
            raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        raise ValueError("Formato invalido")
