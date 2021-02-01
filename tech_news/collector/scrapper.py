import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    print("url " + url)
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    if response.status_code != 200:
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    url_base = "https://www.tecmundo.com.br/novidades"
    page = 1
    news = []
    while page <= pages:
        selector = Selector(fetcher(url_base + "?page=" + str(page)))
        items = selector.css(".tec--list__item")
        for index, item in enumerate(items):
            url = item.css("h3 a::attr(href)").get()
            content = fetcher(url)
            content_selector = Selector(content)

            title = content_selector.css("#js-article-title::text").get()

            timestamp = content_selector.css(
                "#js-article-date::attr(datetime)"
            ).get()

            writer = content_selector.css(
                ".tec--author__info__link::text"
            ).get()

            shares_count = content_selector.css(
                "tec--toolbar__item::text"
            ).get()
            if shares_count is None:
                shares_count = "0"

            comments_count = content_selector.css(
                "#js-comments-btn::attr(data-count)"
            ).get()
            if comments_count is None:
                comments_count = "0"

            summary = content_selector.css(
                ".tec--article__body > p::text"
            ).get()

            sources = content_selector.css(
                "div.z--mb-16 .tec--badge::text"
            ).getall()

            categories = content_selector.css(
                "#js-categories > a::text"
            ).getall()

            obj = {
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
            news.append(obj)
        page += 1
    return news
