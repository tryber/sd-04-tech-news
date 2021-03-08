import requests
import time
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    time.sleep(delay)
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        sleep(delay)
    except (requests.exceptions.HTTPError, requests.exceptions.ReadTimeout):
        return ""
    else:
        return resp.text


def new_object(url, selector):
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    title = selector.css(".tec--article__header__title::text").get()
    writer = selector.css(".tec--author__info__link::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments_count is None:
        comments_count = "0"
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d")
    if shares_count is None:
        shares_count = "0"
    summary = selector.css(".tec--article__body *::text").get()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories .tec--badge::text").getall()
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
    """Seu código deve vir aqui"""
