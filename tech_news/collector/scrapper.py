import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    if response.status_code != 200:
        return ""
    return response.text


def scrape(fetcher, pages=1):
    news = []
    for page in range(pages):
        base_url = "https://www.tecmundo.com.br/novidades?page=" + str(
            page + 1
        )
        print(base_url)
        selector = Selector(fetcher(base_url))
        articles = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()

        for url in articles:
            selector = Selector(fetcher(url))
            # title
            title = selector.css("#js-article-title::text").get()
            # timestamp
            timestamp = selector.css("#js-article-date::attr(datetime)").get()
            # writer
            writer = selector.css(".tec--author__info__link::text").get()
            # share_count
            shares_count = int(
                selector.css(".tec--toolbar__item::text").get().split()[0]
            )
            # comments_count
            comments_count = int(
                selector.css("#js-comments-btn::attr(data-count)").get()
            )
            # summary
            summary = "".join(
                selector.css(
                    ".tec--article__body p:first-of-type ::text"
                ).getall()
            )
            # sources
            sources = selector.css("div.z--mb-16 .tec--badge::text").getall()
            # categories
            categories = selector.css("#js-categories a::text").getall()
            # append to list
            news.append(
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
    return news
