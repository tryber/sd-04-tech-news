import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news


def collector_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair.\n"
    )
    if option == "1":
        filepath = input("Digite o nome do arquivo CSV a ser importado:")
        new_file = csv_importer(filepath)
        create_news(new_file)
    elif option == "2":
        filepath = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(filepath)
    elif option == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas:")
        new_file = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(new_file)
    elif option == "4":
        print("Encerrando script\n")
        return
    else:
        print("Opção inválida", file=sys.stderr)
        return


def analyzer_menu():
    """Seu código deve vir aqui"""
