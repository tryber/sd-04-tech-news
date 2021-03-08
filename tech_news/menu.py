from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
import sys


def collector_menu():
    option = input("""Selecione uma das opções a seguir:
        1 - Importar notícias a partir de um arquivo CSV;
        2 - Exportar notícias para CSV;
        3 - Raspar notícias online;
        4 - Sair.""")
    
    if option == "1":
        file = input("Digite o nome do arquivo CSV a ser importado:")
        action = csv_importer(file)
        return create_news(action)
    elif option == "2":
        file = input("Digite o nome do arquivo CSV a ser exportado:")
        return csv_exporter(file)
    elif option == "3":
        pages = int(input("Digite a quantidade de páginas a serem raspadas:"))
        action = scrape(fetcher=fetch_content, pages=pages)
        return create_news(action)
    elif option == "4":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""
