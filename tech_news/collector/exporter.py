import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, 'w') as csvfile:
        # cabeçalhos
        columns = ['url', 'title', 'timestamp', 'writer', 'shares_count',
                   'comments_count', 'summary', 'sources', 'categories']
        # escreve uma linha com os cabeçalhos no arquivo csv 
        writer = csv.DictWriter(csvfile, fieldnames=columns, delimiter=';')
        writer.writeheader()
        # obtendo os dados do banco
        records = find_news()
        #  juntando os valores das colunas sources:[,] e categories:[,]
        for row in records:
            row["sources"] = ",".join(row["sources"])
            row["categories"] = ",".join(row["categories"])
            # escreve o arquivo csv
            writer.writerow(row)
