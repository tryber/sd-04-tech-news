import requests
from time import sleep
from parsel import Selector

def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    if response.status_code != 200:
        return ""
    else:
        return response.text

# def data_scrape(url, fetcher):
#     selector = Selector(text=fetcher(url))
#     title = selector.css("#js-article-title::text").get()
#     timestamp = selector.css(".tec--timestamp__item time::attr(datetime)").get()
#     writer = selector.css(".tec--author__info__link::text").get()
#     shares_count = selector.css("button::attr(data-count)").get()
#     comments_count = selector.css(".tec--btn::attr(data-count)").get()
#     summary = selector.css(".tec--article__body > p::text").get()
#     sources = selector.css(".z--mb-16 > div a::text").getall()
#     categories = selector.css("#js-categories a::text").getall()
#     return {
#         "url": url,
#         "title": title,
#         "timestamp": timestamp,
#         "writer": writer,
#         "shares_count": int(shares_count),
#         "comments_count": int(comments_count),
#         "summary": summary,
#         "sources": sources,
#         "categories": categories,
#     }

def scrape(fetcher, pages=1):
    data_list = []
    base_url = "https://www.tecmundo.com.br/novidades"
    selector = Selector(fetcher(base_url))
    items = selector.css(".tec--card__info h3 a::attr(href)").getall()

    for item in items:
        content = fetcher(item)
        selector = Selector(text=content)
        title = selector.css("#js-article-title::text").get()
        writer = selector.css(".tec--author__info__link::text").get()
        shares_count = selector.css("button::attr(data-count)").get()
        comments_count = selector.css(".tec--btn::attr(data-count)").get()
        timestamp = selector.css(".tec--timestamp__item time::attr(datetime)").get()
        summary = selector.css(".tec--article__body > p::text").get()
        sources = selector.css(".z--mb-16 > div a::text").getall()
        categories = selector.css("#js-categories a::text").getall()

        data_list.append(
            {
                "url": item,
                "title": title,
                "timestamp": timestamp,
                "writer": writer,
                "shares_count": int(shares_count),
                "comments_count": int(comments_count),
                "summary": summary,
                "sources": sources,
                "categories": categories,
            }
        )
    return data_list
