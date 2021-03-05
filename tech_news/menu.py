from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
""" from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories """
import sys


num_options = """Escolha uma das opções abaixo:

1: Importar notícias a partir de um arquivo CSV
2: Exportar notícias para CSV
3: Raspar notícias online"
4: Sair"""


def first_menu(num):
    print(num)


def open_sec_menu(select, selected):
    if select > 4 or select < 1:
        print(selected[5], file=sys.stderr)
        return

    print(selected[select])
    # segunda opção de menu, de acordo com a var select

    if select > 3:
        return


def collector_menu():
    selected_option = {
        1: "Digite o nome do arquivo CSV a ser importado:",
        2: "Digite o nome do arquivo CSV a ser exportado:",
        3: "Digite a quantidade de páginas a serem raspadas:",
        4: "Encerrando Script",
        5: "Opção inválida",
    }

    first_menu(num_options)  # primeiro menu, 4 opções

    try:
        select = int(input())  # primeira seleção de opção
    except ValueError:
        select = 5

    open_sec_menu(select, selected_option)  # segunda opção de menu

    param_call = input()
    select_functions = {
        1: csv_importer,
        2: csv_exporter,
        3: lambda n: scrape(fetcher=fetch_content, pages=int(n)),
    }
    result = select_functions[select](param_call)
    if select == 3 or select == 1:
        create_news(result)


def analyzer_menu():
    """Seu código deve vir aqui"""
