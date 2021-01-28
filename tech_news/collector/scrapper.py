import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        return ""
    else:
        sleep(delay)
        return response.text


BASE_URL = 'https://www.tecmundo.com.br/novidades'


def scrape(fetcher, pages=1):
    new_list = []
    counter = 1
    while counter <= pages:
        news_response = fetcher(BASE_URL + "?page={page}")
        selector = Selector(text=news_response)

        for new in selector.css(".tec--list__item h3 a::attr(href)").getall():
            new_selector = Selector(text=new)
            new_list.append({
                "url": new,
                "title":
                    new_selector.css(".tec--article__header__title::text")
                    .get(),
                "timestamp":
                    new_selector
                    .css(".tec--timestamp__item time::attr(datetime)")
                    .get(),
                "writer":
                    new_selector.css(".tec--author__info__link::text").get(),
                "shares_count": int(
                    new_selector.css("tec--toolbar__item::text")
                    .re.compile(r"[0-9]+")),
                "comments_count": int(
                    new_selector.css("#js-comments-btn::text")
                    .re.compile(r"[0-9]+")),
                "summary":
                    new_selector.css(".tec--article__body *::text").get(),
                "sources": new_selector.css(".z--mb-16 a::text").getall(),
                "categories":
                    new_selector.css("#js-categories a::text").getall(),
            })
        counter += 1
    return new_list
