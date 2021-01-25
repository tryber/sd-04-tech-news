import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
        response.raise_for_status()
    except requests.ReadTimeout:
        return ""
    except requests.HTTPError:
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    BASE_URL = "https://www.tecmundo.com.br/novidades?page="

    for page in range(1, pages + 1):
        selector_principal = Selector(fetcher(f"{BASE_URL}{page}"))
        list_noticies_URL = selector_principal.css(
            ".tec--card__title a::attr(href)"
        ).getall()

        for i in list_noticies_URL:
            url = i
            selector = Selector(fetcher(url))

            writer = selector.css(".tec--author__info__link::text").get()
            if writer is None:
                writer = selector.css(
                    ".z--items-center .tec--timestamp  .z--font-bold a::text"
                ).get()

            shares_count = selector.css(".tec--toolbar__item::text").get()
            if shares_count is None:
                shares_count = 0
            else:
                shares_count = (
                    selector.css(".tec--toolbar__item::text")
                    .get()
                    .replace(" Compartilharam", "")
                )

            noticies = []

            noticies.append(
                {
                    "url": url,
                    "title": selector.css(
                        ".tec--article__header__title::text"
                    ).get(),
                    "timestamp": selector.css(
                        ".tec--timestamp__item time::attr(datetime)"
                    ).get(),
                    "writer": writer,
                    "shares_count": int(shares_count),
                    "comments_count": int(
                        selector.css(
                            ".tec--toolbar__item button::attr(data-count)"
                        ).get()
                    ),
                    "summary": selector.css(
                        ".tec--article__body *::text"
                    ).get(),
                    "sources": selector.css(".z--mb-16 div *::text").getall(),
                    "categories": selector.css(
                        "#js-categories .tec--badge::text"
                    ).getall(),
                }
            )
            return noticies
