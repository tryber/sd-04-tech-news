def collector_menu():
    """Seu código deve vir aqui"""
    print("Selecione uma das opções a seguir:")
    print(" 1 - Importar notícias a partir de um arquivo CSV;")
    print(
        " 2 - Exportar notícias para CSV;\n 3 - Raspar notícias online;\n 4 - Sair."
    )
    while True:
        try:
            user_choice = int(input("Digite sua opção: "))
        except (TypeError, ValueError, 1 <= user_choice >= 4):
            print("Opção inválida")
            continue
        else:
            print(user_choice)


def analyzer_menu():
    """Seu código deve vir aqui"""
