import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        response = ""
        return response

    if response.status_code != 200:
        response = ""
        return response

    return response.text


# Funções auxiliares para fazer o scrape
def verify_shares_count(shares_count_str):
    """
    Verifica shares_count, pois nem todas as páginas o possuem,
    e colocar seu valor padrão como zero
    """
    if not shares_count_str:
        shares_count = 0
    else:
        shares_count = int(shares_count_str[: -len("Compartilharam")])
    return shares_count


def extract_summary(selector_detail_notice, fetcher, url):
    # Primeiro parágrafo é o resumo
    first_paragraph = selector_detail_notice.css(
        ".tec--article__body > p"
    ).get()
    """
    'first_paragraph' corre o risco de vir 'None',
    caso isso ocorra fazer o requisição novamente
    """
    while first_paragraph is None:
        detail_notice = fetcher(url)
        selector_detail_notice = Selector(text=detail_notice)
        first_paragraph = selector_detail_notice.css(
            ".tec--article__body > p"
        ).get()

    # Texto do primeiro parágrafo dentro de um array
    text_nodes_first_paragraph = (
        Selector(text=first_paragraph).css("*::text").getall()
    )

    # Transformando o resumo em string
    summary = ""
    for phrases in text_nodes_first_paragraph:
        summary += phrases

    return summary


# Para retirar espaços em branco de 'sources', ou 'categories'
"""
def strip_white_spaces(array_of_strings):
    new_array = []
    for element in array_of_strings:
        new_array.append(element.strip())
    return new_array
"""


def scrape(fetcher, pages=1):
    notices = []
    base_url = "https://www.tecmundo.com.br/novidades?page="

    # Percorre o número de páginas dado em 'pages'
    for i in range(1, pages + 1):
        response = fetcher(f"{base_url}{i}")
        selector = Selector(text=response)

        # Links para acesso da notícia
        urls = selector.css(".tec--card__info h3 a::attr(href)").getall()
        for url in urls:
            detail_notice = fetcher(url)
            selector_detail_notice = Selector(text=detail_notice)

            # Título da notícia
            title = selector_detail_notice.css(
                ".tec--article__header__title::text"
            ).get()

            # Data e hora da notícia
            timestamp = selector_detail_notice.css(
                ".tec--timestamp__item time::attr(datetime)"
            ).get()

            # Autor da notícia
            writer = selector_detail_notice.css(
                ".tec--author__info__link::text"
            ).get()

            # shares_count e comments_count são numéricos
            # Número de Compartilhamentos
            shares_count_str = selector_detail_notice.css(
                ".tec--toolbar__item::text"
            ).get()
            shares_count = verify_shares_count(shares_count_str)

            # Número de Comentários
            comments_count_str = selector_detail_notice.css(
                ".tec--toolbar__item button::attr(data-count)"
            ).get()
            comments_count = int(comments_count_str)

            # Primeiro parágrafo é o resumo
            summary = extract_summary(selector_detail_notice, fetcher, url)

            # Fontes
            sources = selector_detail_notice.css(
                ".z--mb-16 div a.tec--badge::text"
            ).getall()

            # Categorias
            categories = selector_detail_notice.css(
                "#js-categories a::text"
            ).getall()

            notices.append(
                {
                    "url": url,
                    "title": title,
                    "timestamp": timestamp,
                    "writer": writer,
                    "shares_count": shares_count,
                    "comments_count": comments_count,
                    "summary": summary,
                    "sources": sources,
                    "categories": categories,
                }
            )

    return notices


# Teste Local
# python3 -i tech_news/collector/scrapper.py
# scrape(fetcher=fetch_content, pages=2)
