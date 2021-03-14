from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_source,
    search_by_title,
)
import sys


def collector_menu():
    entrada = input(
        "Select a option:\n"
        " 1 - Import news from CSV file;\n"
        " 2 - Export News to CSV;\n"
        " 3 - Scrape news;\n 4 - Exit."
    )

    if entrada == "1":
        file_path = input("CSV file name:")
        file_content = csv_importer(file_path)
        create_news(file_content)
    elif entrada == "2":
        file_path = input("Exported CSV file name:")
        csv_exporter(file_path)
    elif entrada == "3":
        pages = input("Number of pages to Scrape:")
        data = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(data)
    elif entrada == "4":
        print("Exit\n")
    else:
        print("Invalid option. Try again.", file=sys.stderr)


def analyzer_menu():
    option = int(
        input(
            "Selecione uma das opções a seguir:\n"
            " 1 - Buscar notícias por título;\n"
            " 2 - Buscar notícias por data;\n"
            " 3 - Buscar notícias por fonte;\n"
            " 4 - Buscar notícias por categoria;\n"
            " 5 - Listar top 5 notícias;\n"
            " 6 - Listar top 5 categorias;\n"
            " 7 - Sair."
        )
    )

    options = {
        1: lambda title: print(search_by_title(title)),
        2: lambda date: print(search_by_date(date)),
        3: lambda source: print(search_by_source(source)),
        4: lambda category: print(search_by_category(category)),
        5: lambda: print(top_5_news()),
        6: lambda: print(top_5_categories()),
        7: lambda: print("Encerrando script\n"),
    }

    string_options = {
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
    }

    if option > 0 and option < 5:
        user_input = input(string_options[option])
        options[option](user_input)
    elif option >= 5 and option < 8:
        options[option]()
    else:
        print("Opção inválida", file=sys.stderr)
