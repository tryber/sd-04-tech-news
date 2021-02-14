import requests
import time
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        time.sleep(delay)
    except requests.exceptions.RequestException:
        return ""
    else:
        return response.text


URL_BASE = "https://www.tecmundo.com.br/novidades"


def scrape_news(url, selector):
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css("a.tec--author__info__link::text").get()
    shares_count = (
        selector.css(".tec--toolbar__item::text").re_first(r"\d") or "0"
    )
    comments_count = (
        selector.css("#js-comments-btn::text").re_first(r"\d") or "0"
    )
    summary = selector.css(".tec--article__body > p::text").get()
    sources = selector.css("div.z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories a::text").getall()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


def scrape(fetcher, pages=1):
    news_object = []
    for page in range(1, pages + 1):
        selector = Selector(fetcher(f"{URL_BASE}?page={page}"))
        get_urls = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()
        for url in get_urls:
            selector = Selector(fetcher(url))
            news_object.append(scrape_news(url, selector))
    return news_object
