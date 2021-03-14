from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
"""from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories"""
import sys


num_options = """Escolha uma das opções abaixo:
1: Importar notícias a partir de um arquivo CSV
2: Exportar notícias para CSV
3: Raspar notícias online"
4: Sair"""

def collector_menu():
    """Seu código deve vir aqui"""
    options = {
        1: "Digite o nome do arquivo CSV a ser importado:",
        2: "Digite o nome do arquivo CSV a ser exportado:",
        3: "Digite a quantidade de páginas a serem raspadas:",
        4: "Encerrando Script",
        5: "Opção inválida"
    }

    print(num_options)

    try:
        items = int(input())
    except ValueError:
        items = 5

    if items > 4 or items < 1:
        print(options[5], file=sys.stderr)
        return

    print(options[items])

    if items > 3:
        return

    param_call = input()
    select_functions = {
        1: csv_importer,
        2: csv_exporter,
        3: lambda n: scrape(fetcher=fetch_content, pages=int(n)),
    }
    result = select_functions[items](param_call)
    if items == 3 or items == 1:
        create_news(result)

def analyzer_menu():
    """Seu código deve vir aqui"""
