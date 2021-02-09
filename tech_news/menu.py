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


def collector_menu():
    # REFERENCIA - https://www.youtube.com/watch?v=OBJL5vPj4-E

    print(
        """Selecione uma das opções a seguir:
 1 - Importar notícias a partir de um arquivo CSV;
 2 - Exportar notícias para CSV;
 3 - Raspar notícias online;
 4 - Sair."""
    )

    # todo input é string, então transofrmo para integer
    user_choice = input()

    if user_choice == "1":
        file = input("Digite o nome do arquivo CSV a ser importado:")
        action = csv_importer(file)
        return create_news(action)
    elif user_choice == "2":
        file = input("Digite o nome do arquivo CSV a ser exportado:")
        return csv_exporter(file)
    elif user_choice == "3":
        pages = int(input("Digite a quantidade de páginas a serem raspadas:"))
        action = scrape(fetcher=fetch_content, pages=pages)
        return create_news(action)
    elif user_choice == "4":
        return print("Encerrando script")
    else:
        # About stderr
        # https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
        return print("Opção inválida", file=sys.stderr)


# REFERENCIA PARA REDUZIR A COMPLEXIDADE DOS IFS
# https://jaxenter.com/implement-switch-case-statement-python-138315.html


def option_one():
    return search_by_title(input("Digite o título:"))


def option_two():
    return search_by_date(input("Digite a data no formato aaaa-mm-dd:"))


def option_three():
    return search_by_source(input("Digite a fonte:"))


def option_four():
    return search_by_category(input("Digite a categoria:"))


def option_seven():
    print("Encerrando script")


def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por fonte;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair.\n "
    )

    user_choice = int(input())

    options = {
        1: option_one,
        2: option_two,
        3: option_three,
        4: option_four,
        5: top_5_news,
        6: top_5_categories,
        7: option_seven,
    }

    try:
        return options[user_choice]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
