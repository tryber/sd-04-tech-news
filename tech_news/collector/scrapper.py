import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(
            "https://www.tecmundo.com.br/novidades", timeout=timeout
        )
        sleep(delay)
        print(response)
    except requests.ReadTimeout:
        return ""
    if response.status_code != 200:
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    url = "https://www.tecmundo.com.br/novidades"
    page = 1
    news = []

    while page <= pages:
        selector = Selector(fetcher(url + "?page=" + str(page)))
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
                "button::attr(data-count)"
            ).get()
            comments_count = content_selector.css(
                "#js-comments-btn::attr(data-count)"
            ).get()
            summary = content_selector.css(
                ".tec--article__body > p::text"
            ).get()
            sources = content_selector.css(".z--m-none > a::text").getall()
            categories = content_selector.css("#js-categories::text").getall()
            obj = {
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
            news.append(obj)
        page += 1
    return news
