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


def analyzer_menu():
    user_input = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )

    if user_input == "1":
        title = input("Digite o título:")
        print(search_by_title(title))
    elif user_input == "2":
        date = input("Digite a data no formato aaaa-mm-dd:")
        print(search_by_date(date))
    elif user_input == "3":
        source = input("Digite a fonte:")
        print(search_by_source(source))
    elif user_input == "4":
        category = input("Digite a categoria:")
        print(search_by_category(category))
    elif user_input == "5":
        print(top_5_news())
    elif user_input == "6":
        print(top_5_categories())
    elif user_input == "7":
        print("Encerrando script\n")
    else:
        print("Opção inválida", file=sys.stderr)
