import requests
import time
from parsel import Selector

BASE_URL = "https://www.tecmundo.com.br/novidades"


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text
    finally:
        time.sleep(delay)


def scrape(fetcher, pages=1):
    list_news = []
    count = 1
    while count <= pages:
        response = fetcher(BASE_URL + "?page={count}")
        selector = Selector(text=response)

        for url in selector.css(".tec--card__title a::attr(href)").getall():
            selector_url = Selector(text=fetcher(url))
            list_news.append(
                {
                    "url": url,
                    "title": selector_url.css("#js-article-title::text").get(),
                    "timestamp": selector_url.css(
                        ".tec--timestamp__item time::attr(datetime)"
                    ).get(),
                    "writer": selector_url.css(
                        ".tec--author__info__link::text"
                    ).get(),
                    "shares_count": selector_url.css(
                        ".tec--toolbar__item::text"
                    ).re_first(r"\d+"),
                    "comments_count": selector_url.css(
                        "#js-comments-btn::text"
                    ).re_first(r"\d+"),
                    "summary": selector_url.css(
                        ".tec--article__body *::text"
                    ).get(),
                    "sources": selector_url.css(".tec--badge::text").getall(),
                    "categories": selector_url.css(
                        "#js-categories a::text"
                    ).getall(),
                }
            )
        count += 1
    return list_news
