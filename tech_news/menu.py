from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
)
import sys


def collector_menu():
    menu = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair.\n"
    )

    if menu == "1":
        file = input("Digite o nome do arquivo CSV a ser importado:")
        new = csv_importer(file)
        create_news(new)
    elif menu == "2":
        file = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(file)
    elif menu == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas:")
        new = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(new)
    elif menu == "4":
        return print("Encerrando script")

    else:
        return print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    menu = input(
        "Selecione uma das opções a seguir:\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por fonte;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair.\n "
    )

    if menu == "1":
        titulo = input("Digite o título: ")
        search_by_title(titulo)
    elif menu == "2":
        data = input("Digite a data no formato aaaa-mm-dd: ")
        search_by_date(data)
    elif menu == "3":
        fonte = input("Digite a fonte: ")
        search_by_source(fonte)
    elif menu == "7":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)
