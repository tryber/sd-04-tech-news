import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        try:
            for line in reader:
                print(line)
        except csv.Error as err:
            print("algum erro rolou...", err)
