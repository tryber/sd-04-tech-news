import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        print("fetching content", url)
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        sleep(delay)
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    base_url = "https://www.tecmundo.com.br/novidades?page="
    page_number = 1

    all_news = []

    while page_number <= pages:
        content = fetcher(f"{base_url}{page_number}")
        selector = Selector(content)
        news_container = selector.css("div.tec--list__item")
        for item in news_container:
            url = selector.css("h3 a::att(href)").get()
            details_content = fetcher(url)
            details_selector = Selector(details_content)
            title = details_selector.css("#js-article-title::text").get()
            timestamp = details_selector.css(
                ".tec--timestamp__item time::attr(datetime)"
            ).get()
            writer = details_selector.css(
                ".tec--author__info__link::text"
            ).get()
            shares = details_selector.css("button::attr(data-count)").get()
            comments = details_selector.css(
                ".tec--btn::attr(data-count)"
            ).getall()
            summary = details_selector.css(
                ".tec--article__body > p::text"
            ).get()
            sources = details_selector.css(".z--mb-16 > div a::text").getall()
            categories = details_selector.css(
                "#js-categories a::text"
            ).getall()

            news = {
                "url": url,
                "title": title,
                "timestamp": timestamp,
                "writer": writer,
                "shares_count": int(shares),
                "comments_count": int(comments[0]),
                "summary": summary,
                "sources": sources,
                "categories": categories,
            }

            all_news.append(news)

        page_number += 1

    return all_news
