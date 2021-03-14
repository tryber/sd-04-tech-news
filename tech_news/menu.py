from tech_news.database import create_news
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content


def collector_menu():
    inputed_value = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair."
    )

    if int(inputed_value) < 3:
        csv_file_path = input("Insira o caminho do arquivo CSV: ")
        if inputed_value == "1":
            return create_news(csv_importer(csv_file_path))
        else:
            return csv_exporter(csv_file_path)
    elif inputed_value == "3":
        number_of_pages = input("insira quantas páginas deseja raspar: ")
        scraped_data = scrape(fetcher=fetch_content, pages=int(number_of_pages))
        return create_news(scraped_data)
    elif inputed_value == "4":
        return print("Script finalizado")


def analyzer_menu():
    """Seu código deve vir aqui"""
