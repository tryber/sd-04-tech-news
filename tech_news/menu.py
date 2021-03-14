from tech_news.database import create_news
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
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
    inputted_option = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair."
    )

    if inputted_option == "1" or inputted_option == "2":
        csv_file_path = input("Insira o caminho do arquivo CSV: ")
        if inputted_option == "1":
            return create_news(csv_importer(csv_file_path))
        else:
            return csv_exporter(csv_file_path)
    elif inputted_option == "3":
        number_of_pages = input("insira quantas páginas deseja raspar: ")
        scraped_data = scrape(
            fetcher=fetch_content, pages=int(number_of_pages)
        )
        return create_news(scraped_data)
    elif inputted_option == "4":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)


functions_by_option = {
    1: lambda title: print(search_by_title(title)),
    2: lambda date: print(search_by_date(date)),
    3: lambda source: print(search_by_source(source)),
    4: lambda category: print(search_by_category(category)),
    5: lambda: print(top_5_news()),
    6: lambda: print(top_5_categories()),
    7: lambda: print("Encerrando script"),
}


def analyzer_menu():
    inputted_option = int(
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

    if inputted_option > 0 and inputted_option < 5:
        inputted_value = input("Insira o valor")
        functions_by_option[inputted_option](inputted_value)
    elif inputted_option < 8:
        functions_by_option[inputted_option]()
    else:
        print("Opção inválida", file=sys.stderr)
