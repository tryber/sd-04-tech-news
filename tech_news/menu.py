from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
import sys


def collector_menu():
    menu = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair.\n"
    )

    if menu == "1":
        file = input("Digite o nome do arquivo CSV a ser importado:")
        new = csv_importer(file)
        create_news(new)
    elif menu == "2":
        file = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(file)
    elif menu == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas:")
        new = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(new)
    elif menu == "4":
        return print("Encerrando script")

    else:
        return print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""
