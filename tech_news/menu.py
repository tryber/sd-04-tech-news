from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories
import sys


num_options = """Escolha uma das opções abaixo:

1: Importar notícias a partir de um arquivo CSV
2: Exportar notícias para CSV
3: Raspar notícias online"
4: Sair"""

selected_option = {
    1: "Digite o nome do arquivo CSV a ser importado:",
    2: "Digite o nome do arquivo CSV a ser exportado:",
    3: "Digite a quantidade de páginas a serem raspadas:",
    4: "Encerrando Script",
    5: "Opção inválida",
}

analyze_option = """Selecione uma das opções a seguir:

 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""


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

# função principal do menu


def collector_menu():

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


def sec_ana_option(num):
    last_options = {
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
        7: "Encerrando script",
        8: "Opção inválida",
    }

    if num > 7 or num < 1:
        print(last_options[8], file=sys.stderr)
        return

    print(last_options[num])


def analyzer_menu():
    """Seu código deve vir aqui"""
    print(analyze_option)

    try:
        ana_input = int(input())
    except ValueError:
        ana_input = 8

    ana_functions = {
        1: search_by_title,
        2: search_by_date,
        3: search_by_source,
        4: search_by_category,
        5: top_5_news,
        6: top_5_categories,
    }

    if ana_input < 5 or ana_input > 6:
        sec_ana_option(ana_input)
        if ana_input > 6 or ana_input < 1:
            return
        param_ana_input = input()
        result = ana_functions[ana_input](param_ana_input)
    else:
        result = ana_functions[ana_input]()

    print(result)
