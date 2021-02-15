from parsel import Selector
from time import sleep
import requests

URL_BASE = "https://www.tecmundo.com.br/novidades"


def fetch_content(url, timeout=3, delay=0.5):
    try:
        sleep(delay)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return ""
    except requests.ReadTimeout:
        return ""


def scrape(fetcher, pages=1):
    list_news = []
    page = 1
    while page <= pages:
        response = fetcher(URL_BASE + "?page={page}")
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
        page += 1
    return list_news
