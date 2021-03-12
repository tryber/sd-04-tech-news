import sys
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.database import create_news

collector_options = """Selecione uma das opções a seguir:
1 - Importar notícias a partir de um arquivo CSV;
2 - Exportar notícias para CSV;
3 - Raspar notícias online;
4 - Sair."""


def collector_menu():
    response = input(collector_options)
    if response == "1":
        file = input("Digite o nome do arquivo CSV a ser importado: ")
        import_csv = csv_importer(file)
        return create_news(import_csv)
    elif response == "2":
        file = input("Digite o nome do arquivo CSV a ser exportado: ")
        return csv_exporter(file)
    elif response == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas: ")
        scraped_news = scrape(fetcher=fetch_content, pages=int(pages))
        return create_news(scraped_news)
    elif response == "4":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""
