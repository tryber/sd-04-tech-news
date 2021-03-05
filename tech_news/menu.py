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


num_options = ("""Escolha uma das opções abaixo:

1: Importar notícias a partir de um arquivo CSV
2: Exportar notícias para CSV
3: Raspar notícias online"
4: Sair""")


def collector_menu():
    selected_option = {
        1: "Digite o nome do arquivo CSV a ser importado:",
        2: "Digite o nome do arquivo CSV a ser exportado:",
        3: "Digite a quantidade de páginas a serem raspadas:",
        4: "Encerrando Script",
        5: "Opção inválida"
    }

    print(num_options)

    try:
        select = int(input())
    except ValueError:
        select = 5

    if select > 4 or select < 1:
        print(selected_option[5], file=sys.stderr)
        return

    print(selected_option[select])

    if select > 3:
        return

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
