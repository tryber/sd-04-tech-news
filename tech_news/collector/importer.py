import csv
# pip install python-csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            # https://docs.python.org/3/library/csv.html#csv.DictReader
            read_content = csv.DictReader(file, delimiter=";")
            content = ""
            for content in read_content:
                values = content
                return [values]
    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")


'''
def headerForm(header):
    if (
        "url"
        and "title"
        and "timestamp"
        and "writer"
        and "shares_count"
        and "comments_count"
        and "summary"
        and "sources"
        and "categories" not in header
    ):
        raise ValueError("Formato invalido")


def format_object(data, header):
    csv_list = []
    for info in data:
        new_obj = {}
        for i in range(len(header)):
            key = header[i]
            new_obj[key] = info[i]
        csv_list.append(new_obj)
    return csv_list


def csv_importer(filepath):
    csv_list = []
    try:
        if not filepath.endswith(".csv"):
            raise ValueError("Formato invalido")
        with open(filepath, "r") as file:
            content = csv.reader(file, delimiter=";", quotechar='"')
            header, *data = content
            headerForm(header)
            csv_list = format_object(data, header)
    except FileNotFoundError:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
    else:
        return csv_list
'''
