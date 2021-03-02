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


def collector_menu(input):
    options = {
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair.\n"
    }

    if options == "1":
        file_path = input("Digite o nome do arquivo CSV a ser importado:")
        new_file = csv_importer(file_path)
        create_news(new_file)
    elif options == "2":
        file_path = input("Digite o nome do Arquivo CSV a ser Exportado:")
        csv_importer(file_path)
    elif options == 3:
        pages = input("Digite a quantidade de páginas a serem raspadas:")
        new_file = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(new_file)
    elif options == "4":
        print("Encerrando script")
    else:
        print("Opção inválida", file=sys.stderr)
        return


def analyzer_menu():
    """Seu código deve vir aqui"""
