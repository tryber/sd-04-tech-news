# modulo que importa/exporta dados no formato csv
# https://docs.python.org/3/library/csv.html
import csv


def csv_importer(filepath):
    try:
        # https://stackoverflow.com/questions/34376441/
        # if-not-condition-statement-in-python/34376465#34376465
        # https://www.w3schools.com/python/ref_string_endswith.asp
        lines = []
        if not filepath.endswith(".csv"):
            # https://docs.python.org/3/tutorial/errors.html (8.4)
            raise ValueError("Formato invalido")
        with open(filepath) as file:
            # https://docs.python.org/3/library/csv.html
            files = csv.DictReader(file, delimiter=";")
            # print(files)
            for line in files:
                lines.append(line)
                # print(f"lineeeee {line}")
            # print(f"printtttttttt {lines}")
            return lines

    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")


# print(csv_importer("correct.csv"))
