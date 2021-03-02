import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
)


def collector_menu():
    menu_options = input(
        "Selecione uma das opções a seguir:\n "
        + "1 - Importar notícias a partir de um arquivo CSV;\n "
        + "2 - Exportar notícias para CSV;\n "
        + "3 - Raspar notícias online;\n "
        + "4 - Sair.\n "
    )

    if menu_options == "1":
        file = input("Digite o nome do arquivo CSV a ser importado: ")
        imported = csv_importer(file)
        return create_news(imported)
    elif menu_options == "2":
        file = input("Digite o nome do arquivo CSV a ser exportado: ")
        return csv_exporter(file)
    elif menu_options == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas: ")
        scraped = scrape(fetcher=fetch_content, pages=int(pages))
        return create_news(scraped)
    elif menu_options == "4":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    second_menu = input(
        "Selecione uma das opções a seguir:\n "
        + "1 - Buscar notícias por título;\n "
        + "2 - Buscar notícias por data;\n "
        + "3 - Buscar notícias por fonte;\n "
        + "4 - Buscar notícias por categoria;\n "
        + "5 - Listar top 5 notícias;\n "
        + "6 - Listar top 5 categorias;\n "
        + "7 - Sair.\n "
    )
    if second_menu == "1":
        title = input("Digite o título: ")
        return search_by_title(title)
    elif second_menu == "2":
        date = input("Digite a data no formato aaaa-mm-dd: ")
        return search_by_date(date)
    elif second_menu == "3":
        source = input("Digite a fonte: ")
        return search_by_source(source)
    elif second_menu == "7":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)
