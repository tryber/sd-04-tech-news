from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news

def collector_option(opt_input):
    all_options = {
        1: "Digite o nome do arquivo CSV a ser importado:",
        2: "Digite o nome do arquivo CSV a ser exportado:",
        3: "Digite a quantidade de páginas a serem raspadas:",
        4: "Encerrando script",
        5: "Opção inválida",
    }

    if opt_input > 4 or opt_input < 1:
        print(all_options[5], file=sys.stderr)
        return

    print(all_options[opt_input])


def collector_menu():
    print(
        """Selecione uma das opções a seguir:
 1 - Importar notícias a partir de um arquivo CSV;
 2 - Exportar notícias para CSV;
 3 - Raspar notícias online;
 4 - Sair."""
    )
    try:
        opt_input = int(input())
    except ValueError:
        opt_input = 5

    collector_option(opt_input)

    if opt_input > 3:
        return

    param_input = input()
    all_functions = {
        1: csv_importer,
        2: csv_exporter,
        3: lambda n: scrape(fetcher=fetch_content, pages=int(n)),
    }
    result = all_functions[opt_input](param_input)
    if opt_input == 3 or opt_input == 1:
        create_news(result)


def analyzer_menu():
    """Seu código deve vir aqui"""
