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
    notices = []
    base_url = "https://www.tecmundo.com.br/novidades?page="

    # Percorre o número de páginas dado em 'pages'
    for i in range(1, pages + 1):
        response = fetcher(f"{base_url}{i}")
        # print("\nRESPONSE:", response)
        selector = Selector(text=response)

        # Links para acesso da notícia
        # urls = selector.css(".tec--card__title a::attr(href)").getall()
        urls = selector.css(".tec--card__info h3 a::attr(href)").getall()
        print("\nLEN_URLS:", len(urls))
        print("URLS:", urls)
        for url in urls:
            # Talvez utilizar o array urls para pegar os outros
            # atributos de cada página, como title e timestamp
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
            # Talvez seja necessário fazer uma verificação do shares_count,
            # pois nem todas as páginas tem,
            # e colocar seu valor padrão como zero
            # Número de Compartilhamentos
            shares_count_str = selector_detail_notice.css(
                ".tec--toolbar__item::text"
            ).get()
            if not shares_count_str:
                shares_count = 0
            else:
                shares_count = int(shares_count_str[: -len("Compartilharam")])
            # Número de Comentários
            comments_count_str = selector_detail_notice.css(
                ".tec--toolbar__item button::attr(data-count)"
            ).get()
            comments_count = int(comments_count_str)
            # Primeiro parágrafo é o resumo
            # Primeiro parágrafo
            # detail_notice = fetcher(url)
            # selector_detail_notice = Selector(text=detail_notice)
            # print("\nSELECTOR_DETAIL_NOTICE:", selector_detail_notice)
            # print("URL:", url)
            first_paragraph = selector_detail_notice.css(
                ".tec--article__body > p"
            ).get()
            while first_paragraph is None:
                detail_notice = fetcher(url)
                selector_detail_notice = Selector(text=detail_notice)
                first_paragraph = selector_detail_notice.css(
                    ".tec--article__body > p"
                ).get()
            # print("\nFIRST_PARAGRAPH:", first_paragraph)
            # Texto do primeiro parágrafo dentro de um array
            text_nodes_first_paragraph = (
                Selector(text=first_paragraph).css("*::text").getall()
            )
            # print("TEXT_NODES_FIRST_PARAGRAPH:", text_nodes_first_paragraph)
            # Transformando o resumo em string
            summary = ""
            for phrases in text_nodes_first_paragraph:
                summary += phrases
            # summary = selector_detail_notice.css(
            #     "div.tec--article__body > p::text").get()
            # print("SUMMARY:", summary)

            # Fontes
            sources = selector_detail_notice.css(
                ".z--mb-16 div a.tec--badge::text"
            ).getall()
            # sources = []
            # # Retira espaço em branco de 'sources'
            # for source in get_sources:
            #     sources.append(source.strip())

            # Categorias
            categories = selector_detail_notice.css(
                "#js-categories a::text"
            ).getall()
            # categories = []
            # Retira espaço em branco de 'categories'
            # for categorie in get_categories:
            #     categories.append(categorie.strip())
            # print("\nURL:", urls[0])
            # print("TITLE:", title)
            # print("TIMESTAMP:", timestamp)
            # print("WRITE:", writer)
            # print("SHARES_COUNT:", shares_count)
            # print("COMMENTS_COUNT:", comments_count)
            # print("\nFIRST_PARAGRAPH:", first_paragraph)
            # print("TEXT_NODES_FIRST_PARAGRAPH:", text_nodes_first_paragraph)
            # print("SUMMARY:", summary)
            # print("SOURCES:", sources)
            # print("CATEGORIES:", categories)
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
            # print("\nNEWS: ", news)

    # print("\nSELECTOR:", detail_notice)
    # print(url)
    # print("\n\nNOTICES:", notices)
    print("\nLEN_NOTICES:", len(notices))
    return notices


# Teste Local
# python3 -i tech_news/collector/scrapper.py
# scrape(fetcher=fetch_content, pages=2)
