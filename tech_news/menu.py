# from tech_news.collector.importer import csv_importer
# from tech_news.collector.exporter import csv_exporter
# from tech_news.collector.scrapper import scrape

import sys


def option_menu(user_choice):

    options = {
        1: "Digite o nome do arquivo CSV a ser importado:",
        2: "Digite o nome do arquivo CSV a ser exportado:",
        3: "Digite a quantidade de páginas a serem raspadas:",
        4: "Encerrando script",
        5: "Opção inválida",
    }

    if 1 < user_choice > 4:
        print(options[5], file=sys.stderr)
        return

    print(options[user_choice])


def collector_menu():
    """Seu código deve vir aqui"""
    print(
        """Selecione uma das opções a seguir:
1 - Importar notícias a partir de um arquivo CSV;
2 - Exportar notícias para CSV;
3 - Raspar notícias online;
4 - Sair.
"""
    )

    try:
        user_choice = int(input())
    except (ValueError):
        print("Opção inválida", file=sys.stderr)
        return

    option_menu(user_choice)

    new_choice = input()

    print(new_choice)

    # if user_choice == 1:
    #     import_file = input()
    #     csv_importer(import_file)
    # elif user_choice == 2:
    #     export_file = input()
    #     csv_exporter(export_file)
    # elif user_choice == 3:
    #     scrape_options = input()
    #     scrape(scrape_options)
    # elif user_choice == 4:
    #     print("Encerrando script")
    # else:
    #     print("Opção inválida")


def analyzer_menu():
    """Seu código deve vir aqui"""


collector_menu()
