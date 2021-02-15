from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news

# from tech_news.analyzer.ratings import top_5_news, top_5_categories
# from tech_news.analyzer.search_engine import (
#     search_by_title,
#     search_by_date,
#     search_by_source,
#     search_by_category,
# )
import sys


def collector_menu():
    print(
        """Selecione uma das opções a seguir:
        1 - Importar notícias a partir de um arquivo CSV;
        2 - Exportar notícias para CSV;
        3 - Raspar notícias online;
        4 - Sair."""
    )
    opt_input = int(input())

    if 1 < opt_input >= 5:
        print("Opção inválida", file=sys.stderr)
        return

    menu_switcher = {
        1: "Digite o nome do arquivo CSV a ser importado:",
        2: "Digite o nome do arquivo CSV a ser exportado:",
        3: "Digite a quantidade de páginas a serem raspadas:",
        4: "Encerrando script",
    }

    func_switcher = {
        1: csv_importer,
        2: csv_exporter,
        3: lambda n: scrape(fetcher=fetch_content, pages=int(n)),
    }

    selected_func = func_switcher.get(opt_input)

    print(menu_switcher.get(opt_input))

    if opt_input == 4:
        return

    opt_input = input()
    result = selected_func(opt_input)
    if opt_input == 3 or opt_input == 1:
        create_news(result)


def analyzer_menu():
    """Seu código deve vir aqui"""


collector_menu()
