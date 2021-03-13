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


def new_object(url, selector):
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d")
    if shares_count is None:
        shares_count = "0"
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments_count is None:
        comments_count = "0"
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


def scrape(fetcher=fetch_content, pages=1):
    new_list = []
    for page in range(1, pages + 1):
        new_resp = fetcher(
            f"https://www.tecmundo.com.br/novidades?page={page}"
        )
        new_selector = Selector(text=new_resp)
        for new in new_selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall():
            resp_new = fetcher(new)
            selector_new = Selector(text=resp_new)
            new_obj = new_object(new, selector_new)
            new_list.append(new_obj)
    return new_list
