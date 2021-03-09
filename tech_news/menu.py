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
    \n 1 - Importar notícias a partir de um arquivo CSV;
    \n 2 - Exportar notícias para CSV;
    \n 3 - Raspar notícias online;
    \n 4 - Sair."""

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
    # print(type(option))
    # print(option)
    # aux2 = int(option)
    # print(type(aux2))
    # print(aux2)
    if option not in {'1', '2', '3', '4'}:
        return print(options[5])

    if int(option) == 4:
        return print('Encerrando script')

    aux = options[int(option)]
    entry = input(aux)
    # return print(entry)

    result = funcs[int(option)](entry)

    if int(option) in {1, 3}:
        create_news(result)
        return True

    return True


def analyzer_menu():

    texto = """Selecione uma das opções a seguir:
    \n 1 - Buscar notícias por título;
    \n 2 - Buscar notícias por data;
    \n 3 - Buscar notícias por fonte;
    \n 4 - Buscar notícias por categoria;
    \n 5 - Listar top 5 notícias;
    \n 6 - Listar top 5 categorias;
    \n 7 - Sair."""

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

    if option not in {'1', '2', '3', '4', '5', '6', '7'}:
        return print(options[8], file=sys.stderr)

    if int(option) == 7:
        return print('Encerrando script')

    if int(option) in {1, 2, 3, 4}:
        aux = options[int(option)]
        entry = input(aux)
        result = funcs[int(option)](entry)
    else:
        result = options[int(option)]()

    return print(result)


if __name__ == '__main__':
    collector_menu()
