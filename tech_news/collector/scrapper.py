import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        # print("fetching...")
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        sleep(delay)
    except requests.exceptions.RequestException:
        # print("exception")
        return ""
    else:
        # print("else")
        return response.text


def create_news_dict(url, selector):
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
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
    BASE_URL = "https://www.tecmundo.com.br/novidades"
    news_list = []
    for page in range(1, pages + 1):
        selector = Selector(fetcher(f"{BASE_URL}?page={page}"))
        urls = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()
        for url in urls:
            selector = Selector(fetcher(url))
            news_list.append(create_news_dict(url, selector))
    return news_list
