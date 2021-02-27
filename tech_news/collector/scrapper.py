import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        response = ""
        return response
    if response.status_code != 200:
        response = ""
        return response
    return response.text


URL = "https://www.tecmundo.com.br/novidades"


def scrape(fetcher, pages=1):
    list_news = []
    for i in range(1, pages + 1):
        response = fetcher(f"{URL}?pages={i}")
        selector = Selector(text=response)
        response_news = selector.css(
            ".tec--card__info h3 a::attr(href)"
        ).getall()
        for url in response_news:
            selector = Selector(fetcher(url))
            title = selector.css("#js-article-title::text").get()
            timestamp = selector.css("#js-article-date::attr(datetime)").get()
            writer = selector.css(".tec--author__info__link::text").get()
            shares_count = int(selector.css(".tec--toolbar__item::text").get())
            comments_count = int(
                selector.css("#js-comments-btn::attr(data-count)").get()
            )
            summary = "".join(
                selector.css(
                    ".tec--article__body p:first-of-type ::text"
                ).getall()
            )
            sources = selector.css("div.z--mb-16 a::text").getall()
            categories = selector.css("#js-categories a::text").getall()
            list_news.append(
                {
                    "url": url,
                    "title": title,
                    "timestamp": timestamp,
                    "writer": writer,
                    "shares_count": shares_count,
                    "comments_count": comments_count,
                    "summary": summary,
                    "sources": sources,
                    "categories": categories,
                }
            )
    return list_news
