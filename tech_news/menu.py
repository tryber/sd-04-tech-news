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
    options = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair.\n"
    )

    if options == "1":
        file_path = input("Digite o nome do arquivo CSV a ser importado:")
        new_file = csv_importer(file_path)
        create_news(new_file)
    elif options == "2":
        file_path = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(file_path)
    elif options == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas:")
        new_file = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(new_file)
    elif options == "4":
        return print("Encerrando script")

    else:
        return print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    options = input(
        "Selecione uma das opções a seguir:\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por fonte;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair.\n "
    )
    if options == "1":
        title = input("Digite o título: ")
        search_by_title(title)
    elif options == "2":
        date = input("Digite a data no formato aaaa-mm-dd: ")
        search_by_date(date)
    elif options == "3":
        source = input("Digite a fonte: ")
        search_by_source(source)
    elif options == "4":
        category = input("Digita a categoria:")
        search_by_category(category)
    elif options == "5":
        return top_5_news()
    elif options == "6":
        return top_5_categories()
    elif options == "7":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)
