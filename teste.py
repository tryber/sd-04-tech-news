import sys


num_options = ("""Escolha uma das opções abaixo:

1: Importar notícias a partir de um arquivo CSV
2: Exportar notícias para CSV
3: Raspar notícias online"
4: Sair""")


def teste_collector():
    """Seu código deve vir aqui"""
    selected_option = {
        1: "Digite o nome do arquivo CSV a ser importado:",
        2: "Digite o nome do arquivo CSV a ser exportado:",
        3: "Digite a quantidade de páginas a serem raspadas:",
        4: "Encerrando Script",
        5: "Opção inválida"
    }

    print(num_options)

    try:
        select = int(input())
    except ValueError:
        select = 5

    if select > 4 or select < 1:
        print(selected_option[5], file=sys.stderr)
        return

    print(selected_option[select])


teste_collector()
