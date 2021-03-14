from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_source,
    search_by_title,
)
from tech_news.analyzer.ratings import top_5_categories, top_5_news
import sys


Menu_de_opc = """Selecione uma das opções a seguir:
 1 - Importar notícias a partir de um arquivo CSV;
 2 - Exportar notícias para CSV;
 3 - Raspar notícias online;
 4 - Sair."""

Menu_de_selecao = [
    "Digite o nome do arquivo CSV a ser importado:",
    "Digite o nome do arquivo CSV a ser exportado:",
    "Digite a quantidade de páginas a serem raspadas:",
]


def filtro_input(input_selecionado, max, min):
    if input_selecionado > max or input_selecionado < min:
        print("Opção inválida", file=sys.stderr)
        return False
    elif input_selecionado == max:
        print("Encerrando script\n")
        return False
    elif input_selecionado == 5 or input_selecionado == 6:
        return False
    else:
        return True


def registra_opc(resp, opc):
    if not opc == 2:
        create_news(resp)


def collector_menu():
    opc_selecionada = input(Menu_de_opc)

    if not opc_selecionada.isnumeric():
        return print("Opção inválida", file=sys.stderr)

    opc_selecionada = int(opc_selecionada)

    if filtro_input(opc_selecionada, 4, 1) is True:
        parametro_selecionado = input(Menu_de_selecao[opc_selecionada - 1])
        Menu_de_execucao = {
            1: csv_importer,
            2: csv_exporter,
            3: lambda n: scrape(fetcher=fetch_content, pages=int(n)),
        }
        resp_final = Menu_de_execucao[opc_selecionada](parametro_selecionado)
        registra_opc(resp_final, opc_selecionada)


Menu_de_analyzer = """Selecione uma das opções a seguir:
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""

Menu_selecao_analyzer = [
    "Digite o título:",
    "Digite a data no formato aaaa-mm-dd:",
    "Digite a fonte:",
    "Digite a categoria",

]


def analyzer_menu():
    opc_selecionada = input(Menu_de_analyzer)

    if not opc_selecionada.isnumeric():
        return print("Opção inválida", file=sys.stderr)

    opc_selecionada = int(opc_selecionada)

    if filtro_input(opc_selecionada, 7, 1) is True:
        opc_index = opc_selecionada - 1
        parametro_selecionado = input(Menu_selecao_analyzer[opc_index])
        Menu_de_execucao = {
            1: search_by_title,
            2: search_by_date,
            3: search_by_source,
            4: search_by_category,
        }
        resp_final = Menu_de_execucao[opc_selecionada](parametro_selecionado)
        print(resp_final)
    elif opc_selecionada == 5:
        print(top_5_news())
    elif opc_selecionada == 6:
        print(top_5_categories())
