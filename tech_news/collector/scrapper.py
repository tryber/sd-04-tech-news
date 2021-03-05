import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    print("Fetching", url)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        sleep(delay)
    except (requests.ReadTimeout, requests.exceptions.HTTPError):
        return ""
    if (response.status_code != 200):
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    BASE_URL = "https://www.tecmundo.com.br/novidades"
    list_news = []
    page = 1
    while page <= pages:
        response = fetcher(BASE_URL + f"?page={page}")
        selector = Selector(text=response)
        list_items = selector.css(".tec--list__item h3 a::attr(href)").getall()
        
        for url in list_items:
            selector_item = Selector(fetcher(url))
            list_news.append({
                "url": url,
                "title": selector_item.css(".tec--article__header__title::text").get(),
                "timestamp": selector_item.css("tec--timestamp__item time::attr(datetime)").get(),
                "writer": selector_item.css("tec--author__info__link::text").get(),
                "shares_count": int(selector_item.css("tec--toolbar__item::text").re_first(r"[0-9]+")),
                "comments_count": int(selector_item.css("#js-comments-btn::text").re_first(r"[0-9]+")),
                "summary": selector_item.css(".tec--article__body *::text").get(),
                "sources": selector_item.css("tec--badge::text").getall(),
                "categories": selector_item.css("js-categories a::text").getall(),
            })
        page += 1
    return list_news

