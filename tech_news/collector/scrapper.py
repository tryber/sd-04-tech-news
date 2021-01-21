import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    page_url = fetcher
    for _ in range(pages):
        selector = Selector(text=page_url)
        for news in selector.css(".tec--card__title"):
            url = news.css("a::attr(href)").get()
            details_selector = Selector(text=fetch_content(url))
            details_selector.css("h1.tec--article__header__title::text").get(),
        next_page_url = selector.css(".tec--btn::attr(href)").get()
        page_url = fetch_content(str(next_page_url))


scrape(fetch_content("https://www.tecmundo.com.br/novidades"))
