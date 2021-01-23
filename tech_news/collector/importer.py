import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        print("filepath", filepath)
        raise ValueError("Formato invalido")

    try:
        file_opened = open(filepath, encoding="utf-8")
        file_read = csv.reader(file_opened, delimiter=";")
        header, *data = file_read
        file_output = []
        temp_list = {}
        for index, item in enumerate(header):
            # temp_list = {item: data[0][index]}
            temp_list[item] = data[0][index]
        file_output.append(temp_list)
        print("Tentativa de abrir arquivo", file_output)

        return file_output
    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")

    else:
        print("arquivo manipulado e fechado com sucesso")
        file_opened.close()
    # finally:
