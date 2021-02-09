import sys


def collector_menu():
    print("""Selecione uma das opções a seguir:
 1 - Importar notícias a partir de um arquivo CSV;
 2 - Exportar notícias para CSV;
 3 - Raspar notícias online;
 4 - Sair.""")

    # todo input é string, então transofrmo para integer
    user_choice = int(input())

    if user_choice == 1:
        input("Digite o nome do arquivo CSV a ser importado:")
    elif user_choice == 2:
        input("Digite o nome do arquivo CSV a ser exportado:")
    elif user_choice == 3:
        input("Digite a quantidade de páginas a serem raspadas:")
    elif user_choice == 4:
        return print("Encerrando script")
    else:
        # About stderr https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
        return print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""
