import requests
from time import sleep
from parsel import Selector
import re


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    url_base = "https://www.tecmundo.com.br/novidades"
    page = 1
    next_page_url = f"?page={page}"
    news = []

    while page <= pages:
        response = fetcher(url_base + next_page_url)
        selector = Selector(text=response)

        selector_attribute = ".tec--list__item h3 a::attr(href)"
        for news_item in selector.css(selector_attribute).getall():
            news_response = fetcher(news_item)
            news_selector = Selector(text=news_response)
            ns = news_selector

            url = news_item
            title = news_selector.css(".tec--article__header__title::text")
            timestamp = ns.css(".tec--timestamp__item time::attr(datetime)")
            writer = news_selector.css(".tec--author__info__link::text")
            shares_count = news_selector.css(".tec--toolbar__item::text")
            comments_count = news_selector.css(".tec--btn::attr(data-count)")
            summary = news_selector.css(".tec--article__body p::text")
            sources = news_selector.css(".z--mb-16 a::text")
            categories = news_selector.css("#js-categories a::text")

            news.append({
                "url": url,
                "title": title.get(),
                "timestamp": timestamp.get(),
                "writer": writer.get(),
                "shares_count": int(re.sub("[^0-9]", "", shares_count.get())),
                "comments_count": int(comments_count.get()),
                "summary": summary.get(),
                "sources": sources.getall(),
                "categories": categories.getall(),
            })
        page += 1
    return news

# re source:
# https://www.codegrepper.com/code-examples/python/extract+number+from+string+in+python
