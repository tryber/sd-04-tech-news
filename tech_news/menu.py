from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
import sys


def collector_menu():
    print(
        """Selecione uma das opções a seguir:
 1 - Importar notícias a partir de um arquivo CSV;
 2 - Exportar notícias para CSV;
 3 - Raspar notícias online;
 4 - Sair."""
    )

    # todo input é string, então transofrmo para integer
    user_choice = int(input())

    if user_choice == 1:
        file = input("Digite o nome do arquivo CSV a ser importado:")
        action = csv_importer(file)
    elif user_choice == 2:
        file = input("Digite o nome do arquivo CSV a ser exportado:")
        return csv_exporter(file)
    elif user_choice == 3:
        pages = int(input("Digite a quantidade de páginas a serem raspadas:"))
        action = scrape(fetcher=fetch_content, pages=pages)
    elif user_choice == 4:
        return print("Encerrando script")
    else:
        # About stderr https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
        return print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""
