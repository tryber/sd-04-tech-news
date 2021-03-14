from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.database import create_news
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_source,
    search_by_title,
)
import sys


def collector_menu():
    user_input = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair."
    )

    if user_input == "1":
        file_path = input("Digite o nome do arquivo CSV a ser importado:")
        file_content = csv_importer(file_path)
        create_news(file_content)
    elif user_input == "2":
        file_path = input("Digite o nome do arquivo CSV a ser exportado:")
        file_content = csv_exporter(file_path)
    elif user_input == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas:")
        result = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(result)
    elif user_input == "4":
        print("Encerrando script\n")
    else:
        print("Opção inválida", file=sys.stderr)


# Tentativa de fazer um switch case


def option_1():
    return search_by_title(input("Digite o título:"))


def option_2():
    return search_by_date(input("Digite a data no formato aaaa-mm-dd:"))


def option_3():
    return search_by_source(input("Digite a fonte:"))


def option_4():
    return search_by_category(input("Digite a categoria:"))


def option_7():
    print("Encerrando script")


def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )

    user_input = int(input())

    options = {
        1: option_1,
        2: option_2,
        3: option_3,
        4: option_4,
        5: top_5_news,
        6: top_5_categories,
        7: option_7,
    }

    if user_input > 0 and user_input < 7:
        return options[user_input]()
    else:
        print("Opção inválida", file=sys.stderr)
