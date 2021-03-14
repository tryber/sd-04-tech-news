import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except (requests.exceptions.ReadTimeout):
        return " "
    else:
        return response.text


def scrape(url, selector):
    """Seu código deve vir aqui"""
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css("a.tec--author__info__link::attr(href)").get()
    shares_count = selector.css("tec--toolbar__item::text").re_first(r'\d')
    if shares_count is None:
        shares_count = "0"
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments_count is None:
        comments_count = "0"
    summary = selector.css(".tec--article__body > p::text").get()
    sources = selector.css(".tec--badge::text").getall()
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

URL = "https://www.tecmundo.com.br/novidades"


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    news = []
    for page in range(1, pages + 1):
        selector = Selector(fetcher(f'{URL}?page={page}'))
        url_names = selector.css(
            "a.tec--list__item .tec--card__title__link::attr(href)"
            ).getall()
        for url in url_names:
            selector = Selector(fetcher(url))
            news.append(get_news_content(url, selector))
    return news
