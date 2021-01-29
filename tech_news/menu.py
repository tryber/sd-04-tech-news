from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content


def collector_menu():
    entrada = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n 4 - Sair."
    )

    if entrada == "1":
        file_path = input("Digite o nome do arquivo CSV a ser importado:")
        return csv_importer(file_path)
    elif entrada == "2":
        file_path = input("Digite o nome do arquivo CSV a ser exportado:")
        return csv_exporter(file_path)
    elif entrada == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas:")
        return scrape(fetch_content, pages=pages)
    elif entrada == "4":
        print("Encerrando script\n")
    else:
        print("Opção inválida\n")


def analyzer_menu():
    """Seu código deve vir aqui"""
