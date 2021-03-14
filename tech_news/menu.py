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


options_menu = """Escolha uma das opções abaixo:
1: Importar notícias a partir de um arquivo CSV
2: Exportar notícias para CSV
3: Raspar notícias online"
4: Sair"""

options_selection = {
    1: "Digite o nome do arquivo CSV a ser importado:",
    2: "Digite o nome do arquivo CSV a ser exportado:",
    3: "Digite a quantidade de páginas a serem raspadas:",
    4: "Encerrando Script",
    5: "Opção inválida",
}

option_analyze = """Selecione uma das opções a seguir:
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""


def first_menu(numbers):
    print(numbers)


def open_sec_menu(select, selected):
    if select > 4 or select < 1:
        print(selected[5], file=sys.stderr)
        return

    print(selected[select])

    if select > 3:
        return


def collector_menu():

    first_menu(options_menu)

    try:
        select = int(input()) 
    except ValueError:
        select = 5

    open_sec_menu(select, options_selection)

    param_call = input()
    select_functions = {
        1: csv_importer,
        2: csv_exporter,
        3: lambda n: scrape(fetcher=fetch_content, pages=int(n)),
    }
    result = select_functions[select](param_call)
    if select == 3 or select == 1:
        create_news(result)


def second_options(numbers):
    last_options = {
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
        7: "Encerrando script",
        8: "Opção inválida",
    }

    if numbers > 7 or numbers < 1:
        print(last_options[8], file=sys.stderr)
        return

    print(last_options[numbers])


def analyzer_menu():
    """Seu código deve vir aqui"""
    print(option_analyze)

    try:
        analyze_input = int(input())
    except ValueError:
        analyze_input = 8

    analyze_options_func = {
        1: search_by_title,
        2: search_by_date,
        3: search_by_source,
        4: search_by_category,
        5: top_5_news,
        6: top_5_categories,
    }

    if analyze_input < 5 or analyze_input > 6:
        second_options(analyze_input)
        if analyze_input > 6 or analyze_input < 1:
            return
        param_analyze_input = input()
        result = analyze_options_func[analyze_input](param_analyze_input)
    else:
        result = analyze_options_func[analyze_input]()

    print(result)