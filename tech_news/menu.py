from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.database import create_news
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


def filtro_input(input_selecionado):
    if input_selecionado > 4 or input_selecionado < 1:
        print("Opção inválida", file=sys.stderr)
        return False
    elif input_selecionado == 4:
        print("Encerrando script\n")
        return False
    else:
        return True


def registro_opc(resp, opc):
    if not opc == 2:
        create_news(resp)


def collector_menu():
    opc_selecionada = input(Menu_de_opc)

    if not opc_selecionada.isnumeric():
        return print("Opção inválida", file=sys.stderr)

    opc_selecionada = int(opc_selecionada)

    if filtro_input(opc_selecionada) is True:
        parametro_selecionado = input(Menu_de_selecao[opc_selecionada - 1])
        Menu_de_execucao = {
            1: csv_importer,
            2: csv_exporter,
            3: lambda n: scrape(fetcher=fetch_content, pages=int(n)),
        }
        resp_final = Menu_de_execucao[opc_selecionada](parametro_selecionado)
        registro_opc(resp_final, opc_selecionada)



def analyzer_menu():
    """Seu código deve vir aqui"""
