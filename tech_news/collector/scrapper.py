import requests
import time
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    time.sleep(delay)

    try:
        response = requests.get(url, timeout=timeout)

    except requests.ReadTimeout:
        response = requests.get(url)

    finally:
        return response.text if response.status_code == 200 else ""


def scrape(fetcher=fetch_content, pages=1):

    news_return = []

    for page in range(1, pages + 1):
        response = fetcher(
            "https://www.tecmundo.com.br/novidades?page=" + str(page)
        )
        selector = Selector(text=response)

        urls = selector.css(".tec--card__title__link::attr(href)").getall()

        for url in urls:
            news_return.append(scrape_single_news(url))

    return news_return


def get_title(selector):
    return selector.css("#js-article-title::text").get()


def get_timestamp(selector):
    return selector.css("#js-article-date::attr(datetime)").get()


def get_writer(selector):
    writer = selector.css(".tec--author__info__link::text").get()
    if writer is not None:
        writer = writer.strip()

    return writer


def get_shares_count(selector):
    shares_count = selector.css(".tec--toolbar__item::text")

    if shares_count != []:
        shares_count = int(
            shares_count.get().strip().split()[0],
            base=10,
        )
    return shares_count


def get_comments_count(selector):
    comments_count = selector.css(
        ".tec--toolbar__item > button::text"
    ).getall()

    if comments_count is not None:
        comments_count = int(
            comments_count[1].strip().split()[0],
            base=10,
        )

    return comments_count


def get_summary(selector):
    return "".join(
        selector.css(".tec--article__body p:first-of-type *::text").getall()
    )


def get_sources(selector):
    sources = selector.css(".tec--badge::text").getall()

    for index, source in enumerate(sources):
        sources[index] = source.strip()

    return sources


def get_categories(selector):
    categories = selector.css("#js-categories a::text").getall()

    for index, category in enumerate(categories):
        categories[index] = category.strip()

    return categories


def scrape_single_news(url, fetcher=fetch_content):
    fetch = fetcher(url)
    selector = Selector(text=fetch)

    title = get_title(selector)
    timestamp = get_timestamp(selector)
    writer = get_writer(selector)
    shares_count = get_shares_count(selector)
    comments_count = get_comments_count(selector)
    summary = get_summary(selector)
    categories = get_categories(selector)
    sources = [
        source for source in get_sources(selector) if source not in categories
    ]

    return {
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
