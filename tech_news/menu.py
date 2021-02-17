import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news


def collector_menu():
    menu = (
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair."
    )

    options_to_select = {
        "1": "Digite o nome do arquivo CSV a ser importado:",
        "2": "Digite o nome do arquivo CSV a ser exportado:",
        "3": "Digite a quantidade de páginas a serem raspadas:",
        "4": "Encerrando script\n",
        "5": "Opção inválida"
    }

    functions = {
        "1": csv_importer,
        "2": csv_exporter,
        "3": lambda p: scrape(fetcher=fetch_content, pages=int(p)),
    }

    option = input(menu)
    try:
        print(options_to_select[option])
        if int(option) < 1 or int(option) > 4:
            return print(options_to_select["5"], file=sys.stderr)
    except KeyError:
        return options_to_select["5"]

    # Encerra o script
    if int(option) > 3:
        return

    option_function = input()
    result = functions[option](option_function)
    if int(option) == 1 or int(option) == 3:
        create_news(result)


def analyzer_menu():
    """Seu código deve vir aqui"""


# Teste local
# tech-news-collector
