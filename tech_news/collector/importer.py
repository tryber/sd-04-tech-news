import csv

# https://www.youtube.com/watch?v=pTT7HMqDnJw
# https://realpython.com/python-enumerate/


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        file = open(filepath, encoding="utf-8")
        csv_reader = csv.reader(file, delimiter=";")
        header = next(csv_reader)
        data = [row for row in csv_reader]
        dataArray = []
        builtData = {}
        for index, item in enumerate(header):
            builtData[item] = data[0][index]
        dataArray.append(builtData)
        return dataArray
    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
