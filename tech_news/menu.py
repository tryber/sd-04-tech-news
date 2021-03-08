from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content, scrape
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories
import sys


def scrap(num):
    print(num)
    scrape(fetcher=fetch_content, pages=int(num))


def collector_menu():

    texto = """Selecione uma das opções a seguir:
              1 - Importar notícias a partir de um arquivo CSV;
              2 - Exportar notícias para CSV;
              3 - Raspar notícias online;
              4 - Sair."""

    options = {
        1: "Digite o nome do arquivo CSV a ser importado:",
        2: "Digite o nome do arquivo CSV a ser exportado:",
        3: "Digite a quantidade de páginas a serem raspadas:",
        4: "Encerrando script",
        5: "Opção inválida",
     }

    funcs = {
        1: csv_importer,
        2: csv_exporter,
        3: scrap,
    }

    option = input(texto)

    if int(float(option)) not in {1, 2, 3, 4}:
        return print(options[5])

    if int(float(option)) == 4:
        return print('Encerrando script')

    aux = options[int(float(option))]
    entry = input(aux)
    # return print(entry)

    result = funcs[int(float(option))](entry)

    if int(float(option)) in {1, 3}:
        create_news(result)
        return True

    return True


def analyzer_menu():

    texto = """Selecione uma das opções a seguir:
            1 - Buscar notícias por título;
            2 - Buscar notícias por data;
            3 - Buscar notícias por fonte;
            4 - Buscar notícias por categoria;
            5 - Listar top 5 notícias;
            6 - Listar top 5 categorias;
            7 - Sair."""

    options = {
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
        7: "Encerrando script",
        8: "Opção inválida",
    }

    funcs = {
        1: search_by_title,
        2: search_by_date,
        3: search_by_source,
        4: search_by_category,
        5: top_5_news,
        6: top_5_categories,
    }

    option = input(texto)

    if int(float(option)) not in {1, 2, 3, 4, 5, 6, 7}:
        return print(options[8], file=sys.stderr)

    if int(float(option)) == 7:
        return print('Encerrando script')

    if int(float(option)) in {1, 2, 3, 4}:
        aux = options[int(float(option))]
        entry = input(aux)
        result = funcs[int(float(option))](entry)
    else:
        result = options[int(float(option))]()

    return print(result)


collector_menu()
