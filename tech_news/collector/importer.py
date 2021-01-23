# https://stackoverflow.com/questions/33962267/python-return-error-from-function#:~:text=In%20python%20code%2C%20error%20conditions,it%20reaches%20a%20except%20statement.
# https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
# https://stackoverflow.com/questions/57007680/how-to-handle-the-exception-when-input-file-does-not-exists-in-python/57007738
import csv

def csv_importer(filepath):
    try:
        if not filepath.endswith(".csv"):
            raise ValueError("Formato invalido")
        with open(filepath) as file:
            news = csv.DictReader(file, delimiter=";")
            values = [value for value in news]
    except FileNotFoundError:
        raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
    else:
        return values
