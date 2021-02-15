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


def scrape(fetcher, pages=1):
    news = []
    base_url = "https://www.tecmundo.com.br/novidades?page="
    response = fetcher(f"{base_url}{pages}")
    # print("\nRESPONSE:", response)
    selector = Selector(text=response)

    # Links para acesso da notícia
    urls = selector.css(".tec--card__title a::attr(href)").getall()

    # Talvez utilizar o array urls para pegar os outros
    # atributos de cada página, como title e timestamp
    detail_notice = fetcher(urls[0])
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
    writer = selector_detail_notice.css(".tec--author__info__link::text").get()

    # shares_count e comments_count são numéricos
    # Talvez seja necessário fazer uma verificação do shares_count,
    # pois nem todas as páginas tem, e colocar seu valor padrão como zero
    # Número de Compartilhamentos
    shares_count = int(
        selector_detail_notice.css(".tec--toolbar__item::text").get()[
            : -len("Compartilharam")
        ]
    )
    # Número de Comentários
    comments_count = int(
        selector_detail_notice.css(
            ".tec--toolbar__item button::attr(data-count)"
        ).get()
    )
    # Primeiro parágrafo é o resumo
    # Primeiro parágrafo
    first_paragraph = selector_detail_notice.css(".tec--article__body p").get()
    # Texto do primeiro parágrafo dentro de um array
    text_nodes_first_paragraph = (
        Selector(text=first_paragraph).css("*::text").getall()
    )
    # Transformando o resumo em string
    summary = ""
    for phrases in text_nodes_first_paragraph:
        summary += phrases

    # Fontes
    get_sources = selector_detail_notice.css(
        ".z--mb-16 div a.tec--badge::text"
    ).getall()
    sources = []
    for source in get_sources:
        sources.append(source.strip())

    # Categorias
    get_categories = selector_detail_notice.css(
        "#js-categories a::text"
    ).getall()
    categories = []
    for categorie in get_categories:
        categories.append(categorie.strip())
    print("\nURL:", urls[0])
    print("TITLE:", title)
    print("TIMESTAMP:", timestamp)
    print("WRITE:", writer)
    print("SHARES_COUNT:", shares_count)
    print("COMMENTS_COUNT:", comments_count)
    # print("\nFIRST_PARAGRAPH:", first_paragraph)
    # print("TEXT_NODES_FIRST_PARAGRAPH:", text_nodes_first_paragraph)
    print("SUMMARY:", summary)
    print("SOURCES:", sources)
    print("CATEGORIES:", categories)
    news.append({
        "url": urls[0],
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories
    })
    print("\nNEWS: ", news)
    # news.append(new)
    # url = selector.css(".tec--list").getall()
    # print("\nSELECTOR:", detail_notice)
    # print(url)
    return selector


# Teste Local
# python3 -i tech_news/collector/scrapper.py
# scrape(fetcher=fetch_content, pages=2)
