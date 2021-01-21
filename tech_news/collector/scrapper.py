import requests
from time import sleep
from parsel import Selector

BASE_URL = "https://www.tecmundo.com.br/novidades"


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        return ""
    else:
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    news = []
    page = 1
    while page <= pages:
        news_response = fetcher(BASE_URL + "?page={page}")
        selector = Selector(text=news_response)
        for new in selector.css(".tec--list__item h3 a::attr(href)").getall():
            news_selector = Selector(text=fetcher(new))
            news.append({
                "url": new,
                "title": news_selector.css(".tec--article__header__title::text").get(),
                "timestamp": news_selector.css(".tec--timestamp__item time::attr(datetime)").get(),
                "writer": news_selector.css(".tec--author__info__link::text").get(),
                "shares_count": int(news_selector.css(".tec--toolbar__item::text").re_first(r"[0-9]+")),
                "comments_count": int(news_selector.css("#js-comments-btn::text").re_first(r"[0-9]+")),
                "summary": news_selector.css(".tec--article__body *::text").get(),
                "sources": news_selector.css(".z--mb-16 a::text").getall(),
                "categories": news_selector.css("#js-categories a::text").getall()
            })
        page += 1
    return news
