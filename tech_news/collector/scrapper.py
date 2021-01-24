import requests
import time
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):

    try:
        response = requests.get(url, timeout=timeout)

    except requests.ReadTimeout:
        time.sleep(delay)
        response = requests.get(url, timeout=timeout)

    finally:
        return response.text if response.status_code == 200 else ""


def scrape(fetcher=fetch_content, pages=1):

    news_return = []

    for page in range(1, pages + 1):
        print(page)
        response = fetcher(
            "https://www.tecmundo.com.br/novidades?page=" + str(page)
        )
        selector = Selector(text=response)

        urls = selector.css(".tec--card__title__link::attr(href)").getall()

        for url in urls:

            fetch = fetcher(url)
            selector = Selector(text=fetch)

            title = selector.css("#js-article-title::text").get()

            timestamp = selector.css("#js-article-date::attr(datetime)").get()

            writer = (
                selector.css(".tec--author__info__link::text").get().strip()
                if selector.css(".tec--author__info__link::text").get() != None
                else "None"
            )

            shares_count = (
                int(
                    selector.css(".tec--toolbar__item::text")
                    .get()
                    .strip()
                    .split()[0],
                    base=10,
                )
                if selector.css(".tec--toolbar__item::text").get() != None
                else "None"
            )

            comments_count = (
                int(
                    selector.css(".tec--toolbar__item > button::text")
                    .getall()[1]
                    .strip()
                    .split()[0],
                    base=10,
                )
                if selector.css(".tec--toolbar__item > button::text").getall()
                != None
                else "None"
            )

            summary = "".join(
                selector.css(
                    ".tec--article__body p:first-of-type *::text"
                ).getall()
            )

            sources = selector.css(".tec--badge::text").getall()

            categories = selector.css("#js-categories a::text").getall()

            for index, category in enumerate(categories):
                categories[index] = category.strip()

            for index, source in enumerate(sources):
                sources[index] = source.strip()

            sources = [
                source for source in sources if source not in categories
            ]

            news_return.append(
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

    return news_return
