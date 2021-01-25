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


def collector_option(opt_input):
    all_options = {
        1: "Digite o nome do arquivo CSV a ser importado:",
        2: "Digite o nome do arquivo CSV a ser exportado:",
        3: "Digite a quantidade de páginas a serem raspadas:",
        4: "Encerrando script",
        5: "Opção inválida",
    }

    if opt_input > 4 or opt_input < 1:
        print(all_options[5], file=sys.stderr)
        return

    print(all_options[opt_input])


def collector_menu():
    print(
        "Selecione uma das opções a seguir:\n 1 - Importar notícias a partir de um arquivo CSV;\n 2 - Exportar notícias para CSV;\n 3 - Raspar notícias online;\n 4 - Sair."
    )
    try:
        opt_input = int(input())
    except ValueError:
        opt_input = 5

    collector_option(opt_input)

    if opt_input > 3:
        return

    param_input = input()
    all_functions = {
        1: csv_importer,
        2: csv_exporter,
        3: lambda n: scrape(fetcher=fetch_content, pages=int(n)),
    }
    result = all_functions[opt_input](param_input)
    if opt_input == 3 or opt_input == 1:
        create_news(result)


def analyzer_option(opt_input):
    all_options = {
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
        7: "Encerrando script",
        8: "Opção inválida",
    }

    if opt_input > 7 or opt_input < 1:
        print(all_options[8], file=sys.stderr)
        return

    print(all_options[opt_input])


def analyzer_menu():
    # isso ta horrivel meu amigo quanto if ;--; vou refatorar não, sorry
    print(
        "Selecione uma das opções a seguir:\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n 3 - Buscar notícias por fonte;\n 4 - Buscar notícias por categoria;\n 5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    )
    try:
        opt_input = int(input())
    except ValueError:
        opt_input = 8

    all_functions = {
        1: search_by_title,
        2: search_by_date,
        3: search_by_source,
        4: search_by_category,
        5: top_5_news,
        6: top_5_categories,
    }

    if opt_input < 5 or opt_input > 6:
        analyzer_option(opt_input)
        if opt_input > 6 or opt_input < 1:
            return
        param_input = input()
        result = all_functions[opt_input](param_input)
    else:
        result = all_functions[opt_input]()

    print(result)
