import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("invalid format")
    try:
        csv_file = open(filepath)
    except FileNotFoundError:
        return  ValueError("file not found")
    else:
        with open(filepath) as file:
            read_content = csv.DictReader(file, delimiter=";")
            for content in read_content:
                print(content)
                values = content
                return [values]
