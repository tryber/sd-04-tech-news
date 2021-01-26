import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        """requisição do tipo GET"""
        response = requests.get(url, timeout=timeout)
        """Coloca uma pausa de 0.5 segundos a cada requisição"""
        sleep(delay)
        """pedindo que a resposta lance uma exceção se o status não seja ok"""
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        """Em caso de erro retorna uma string vazia"""
        return ""
    else:
        """conteudo recebido da requisição"""
        return response.text


def scrape(fetcher, pages=1):
    URL_BASE = "https://www.tecmundo.com.br/novidades"
    tech_news_list = []

    for page in range(1, pages + 1):
        main_selector = Selector(fetcher(f"{URL_BASE}?page={page}"))
        articles_url_list = main_selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()

        for url in articles_url_list:
            snd_selector = Selector(fetcher(url))

            writer = snd_selector.css(".tec--author__info__link::text").get()
            if writer is None:
                writer = snd_selector.css(
                    ".z--items-center .tec--timestamp  .z--font-bold a::text"
                ).get()

            shares_count = snd_selector.css(".tec--toolbar__item::text").get()
            if shares_count is None:
                shares_count = 0
            else:
                shares_count = (
                    snd_selector.css(".tec--toolbar__item::text")
                    .get()
                    .replace(" Compartilharam", "")
                )

            tech_news_list.append(
                {
                    "url": url,
                    "title": snd_selector.css(
                        ".tec--article__header__title::text"
                    ).get(),
                    "timestamp": snd_selector.css(
                        ".tec--timestamp__item time::attr(datetime)"
                    ).get(),
                    "writer": writer,
                    "shares_count": int(shares_count),
                    "comments_count": int(
                        snd_selector.css(
                            ".tec--toolbar__item button::attr(data-count)"
                        ).get()
                    ),
                    "summary": snd_selector.css(
                        ".tec--article__body *::text"
                    ).get(),
                    "sources": snd_selector.css(
                        "div.z--mb-16 .tec--badge::text"
                    ).getall(),
                    "categories": snd_selector.css(
                        "#js-categories .tec--badge::text"
                    ).getall(),
                }
            )
    return tech_news_list
