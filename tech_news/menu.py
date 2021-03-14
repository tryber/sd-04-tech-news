from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.database import create_news
from tech_news.collector.scrapper import scrape, fetch_content
import sys


def collector_menu():
    user_input = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair."
    )

    if user_input == "1":
        file_path = input("Digite o nome do arquivo CSV a ser importado:")
        file_content = csv_importer(file_path)
        create_news(file_content)
    elif user_input == "2":
        file_path = input("Digite o nome do arquivo CSV a ser exportado:")
        file_content = csv_exporter(file_path)
    elif user_input == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas:")
        result = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(result)
    elif user_input == "4":
        print("Encerrando script\n")
    else:
        print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""
