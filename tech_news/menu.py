import sys
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


def collector_menu():
    menu_options = (
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair."
    )

    options_to_select = {
        "1": "Digite o nome do arquivo CSV a ser importado:",
        "2": "Digite o nome do arquivo CSV a ser exportado:",
        "3": "Digite a quantidade de páginas a serem raspadas:",
        "4": "Encerrando script\n",
    }

    actions = {
        "1": csv_importer,
        "2": csv_exporter,
        "3": lambda p: scrape(fetcher=fetch_content, pages=int(p)),
    }

    option = input(menu_options)
    try:
        print(options_to_select[option])
    except KeyError:
        return sys.stderr.write("Opção inválida\n")

    # Encerra o script
    if int(option) == 4:
        return

    option_action = input()
    result = actions[option](option_action)
    if int(option) == 1 or int(option) == 3:
        create_news(result)


def analyzer_menu():
    menu_options = (
        "Selecione uma das opções a seguir:\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )

    options_to_select = {
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a fonte:",
        "4": "Digite a categoria:",
        "5": "5",
        "6": "6",
        "7": "Encerrando script\n",
    }

    actions = {
        "1": search_by_title,
        "2": search_by_date,
        "3": search_by_source,
        "4": search_by_category,
        "5": top_5_news,
        "6": top_5_categories,
    }

    option = input(menu_options)
    try:
        print(options_to_select[option])
    except KeyError:
        return sys.stderr.write("Opção inválida\n")

    # Encerra o script
    if int(option) == 7:
        return

    option_action = input()
    result = actions[option](option_action)
    return result


# Teste local
# tech-news-collector
# tech-news-analyzer
