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
    URL = "https://www.tecmundo.com.br/novidades?page="
    news = []

    for page in range(1, pages + 1):
        url_selector = Selector(fetcher(f"{URL}{page}"))
        news_urls_list = url_selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()

        for news_url in news_urls_list:
            selector = Selector(fetcher(news_url))

            shares_count = selector.css(".tec--toolbar__item::text").get()
            if shares_count is None:
                shares_count = 0
            else:
                shares_count = int(
                    (
                        selector.css(".tec--toolbar__item::text")
                        .get()
                        .replace(" Compartilharam", "")
                    )
                )

            news.append(
                {
                    "url": news_url,
                    "title": selector.css(
                        ".tec--article__header__title::text"
                    ).get(),
                    "timestamp": selector.css(
                        ".tec--timestamp__item time::attr(datetime)"
                    ).get(),
                    "writer": selector.css(
                        ".tec--author__info__link::text"
                    ).get(),
                    "shares_count": shares_count,
                    "comments_count": int(
                        selector.css(
                            ".tec--toolbar__item button::attr(data-count)"
                        ).get()
                    ),
                    "summary": selector.css(
                        ".tec--article__body *::text"
                    ).get(),
                    "sources": selector.css(
                        "div.z--mb-16 .tec--badge::text"
                    ).getall(),
                    "categories": selector.css(
                        "#js-categories .tec--badge::text"
                    ).getall(),
                }
            )
    return news
