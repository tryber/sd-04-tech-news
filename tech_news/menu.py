from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content, scrape
from tech_news.database import create_news

def scrap(num):
    print(num)
    scrape(fetcher=fetch_content, pages=int(num))


def collector_menu():

    texto = """Selecione uma das opções a seguir:
              1 - Importar notícias a partir de um arquivo CSV;
              2 - Exportar notícias para CSV;
              3 - Raspar notícias online;
              4 - Sair."""

    all_options = {
        1: "Digite o nome do arquivo CSV a ser importado:",
        2: "Digite o nome do arquivo CSV a ser exportado:",
        3: "Digite a quantidade de páginas a serem raspadas:",
        4: "Encerrando script",
        5: "Opção inválida",
     }

    all_funcs = {
        1: csv_importer,
        2: csv_exporter,
        3: scrap,
    }

    option = input(texto)

    if int(option) not in {1, 2, 3, 4}:
        return print(all_options[5])

    if int(option) == 4:
        return print('Encerrando script')

    aux = all_options[int(option)]
    entry = input(aux)
    # return print(entry)

    result = all_funcs[int(option)](entry)

    if int(option) in {1, 3}:
        create_news(result)
        return True

    return True


def analyzer_menu():
    """Seu código deve vir aqui"""


collector_menu()
