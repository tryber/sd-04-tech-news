from tech_news.collector.importer import csv_importer


def collector_menu():
    entrada = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n 4 - Sair."
    )

    if entrada == "1":
        return csv_importer("correct.csv")
    elif entrada == "2":
        pass
    elif entrada == "3":
        pass
    elif entrada == "4":
        print("Encerrando script\n")
    else:
        print("Opção inválida\n")


def analyzer_menu():
    """Seu código deve vir aqui"""
