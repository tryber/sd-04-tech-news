from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
import sys


def collector_menu():
    """Seu código deve vir aqui"""


def analyzer_option(opt_input):
    all_options = {
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
        7: "Encerrando script",
        8: "Opção inválida",
    }

    if opt_input > 7 or opt_input < 1:
        print(all_options[8], file=sys.stderr)
        return

    print(all_options[opt_input])


def analyzer_menu():
    print(
        """Selecione uma das opções a seguir:
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""
    )
    try:
        opt_input = int(input())
    except ValueError:
        opt_input = 8

    all_functions = {
        1: search_by_title,
        2: search_by_date,
        3: search_by_source,
        4: search_by_category,
        5: top_5_news,
        6: top_5_categories,
    }

    if opt_input < 5 or opt_input > 6:
        analyzer_option(opt_input)
        if opt_input > 6 or opt_input < 1:
            return
        param_input = input()
        result = all_functions[opt_input](param_input)
    else:
        result = all_functions[opt_input]()

    print(result)
