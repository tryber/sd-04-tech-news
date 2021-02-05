from collector.importer import csv_importer
from collector.exporter import csv_exporter
from collector.scrapper import scrape


def collector_menu():
    """Seu código deve vir aqui"""
    print("Selecione uma das opções a seguir:")
    print(" 1 - Importar notícias a partir de um arquivo CSV;")
    print(" 2 - Exportar notícias para CSV;\n 3 - Raspar notícias online;")
    print(" 4 - Sair.")

    while True:
        try:
            user_choice = int(input("Digite sua opção: "))
        except (TypeError, ValueError):
            print("Opção inválida")
            continue
        else:
            # return user_choice
            # print(user_choice)
            if user_choice == 1:
                import_file = input(
                    "Digite o nome do arquivo CSV a ser importado:"
                )
                csv_importer(import_file)
            elif user_choice == 2:
                export_file = input(
                    "Digite o nome do arquivo CSV a ser exportado:"
                )
                csv_exporter(export_file)
            elif user_choice == 3:
                scrape_options = input(
                    "Digite a quantidade de páginas a serem raspadas:"
                )
                scrape(scrape_options)
            elif user_choice == 4:
                print("Encerrando script")
                break
            else:
                print("Opção inválida")


def analyzer_menu():
    """Seu código deve vir aqui"""
