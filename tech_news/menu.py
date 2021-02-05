from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape

import sys

options = {
    1: "Digite o nome do arquivo CSV a ser importado:",
    2: "Digite o nome do arquivo CSV a ser exportado:",
    3: "Digite a quantidade de páginas a serem raspadas:",
}


def collector_menu():
    """Seu código deve vir aqui"""
    print("Selecione uma das opções a seguir:")
    print(" 1 - Importar notícias a partir de um arquivo CSV;")
    print(" 2 - Exportar notícias para CSV;\n 3 - Raspar notícias online;")
    print(" 4 - Sair.")

    try:
        user_choice = int(input())
    except (ValueError):
        print("Opção inválida", file=sys.stderr)
        return

    if user_choice == 1:
        import_file = input()
        csv_importer(import_file)
    elif user_choice == 2:
        export_file = input()
        csv_exporter(export_file)
    elif user_choice == 3:
        scrape_options = input()
        scrape(scrape_options)
    elif user_choice == 4:
        print("Encerrando script")
    else:
        print("Opção inválida")


def analyzer_menu():
    """Seu código deve vir aqui"""
