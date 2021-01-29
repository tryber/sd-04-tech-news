import requests
import time
from parsel import Selector

BASE_URL = "https://www.tecmundo.com.br/novidades"


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.exceptions.HTTPError):
        return ""
    else:
        time.sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    list_news = []
    count = 1
    while count <= pages:
        response = fetcher(BASE_URL + "?page={count}")
        selector = Selector(text=response)

        for url in selector.css(".tec--list__item h3 a::attr(href)").getall():
            selector_url = Selector(text=fetcher(url))
            list_news.append(
                {
                    "url": url,
                    "title": selector_url.css(
                        ".tec--article__header__title::text"
                    ).get(),
                    "timestamp": selector_url.css(
                        ".tec--timestamp__item time::attr(datetime)"
                    ).get(),
                    "writer": selector_url.css(
                        ".tec--author__info__link::text"
                    ).get(),
                    "shares_count": int(
                        selector_url.css(".tec--toolbar__item::text").re_first(
                            r"[0-9]+"
                        )
                    ),
                    "comments_count": int(
                        selector_url.css("#js-comments-btn::text").re_first(
                            r"[0-9]+"
                        )
                    ),
                    "summary": selector_url.css(
                        ".tec--article__body *::text"
                    ).get(),
                    "sources": selector_url.css(".z--mb-16 a::text").getall(),
                    "categories": selector_url.css(
                        "#js-categories a::text"
                    ).getall(),
                }
            )
        count += 1
    return list_news
