from csv import DictReader


def csv_importer(filepath):
    try:
        if filepath.lower().endswith(".csv"):
            with open(filepath) as file:
                news = DictReader(file, delimiter=";", quotechar='"')
                result = [new for new in news]
        else:
            raise ValueError("Formato invalido")
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        return result
