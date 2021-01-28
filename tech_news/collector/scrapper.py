import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        sleep(delay)
        return ""
    else:
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    pages_details = []
    base_url = "https://www.tecmundo.com.br/novidades?page="
    for page_num in range(1, pages + 1):
        selector = Selector(text=fetcher(base_url + str(page_num)))
        for news in selector.css("h3.tec--card__title"):
            url = news.css("a::attr(href)").get()
            details_selector = Selector(text=fetcher(url))
            title = str(
                details_selector.css(
                    "h1.tec--article__header__title::text"
                ).get()
            )
            timestamp = str(
                details_selector.css("#js-article-date::attr(datetime)").get()
            )
            writer = str(
                details_selector.css(".tec--author__info__link::text").get()
            )
            shares_count = str(
                details_selector.css(".tec--toolbar__item::text").get()
            )
            comments_count = str(
                details_selector.css(
                    "#js-comments-btn::attr(data-count)"
                ).get()
            )
            summary = str(
                details_selector.css(".tec--article__body p *::text").get()
            )
            sources = details_selector.css(
                ".z--mb-16 .tec--badge::text"
            ).getall()
            categories = details_selector.css(
                "#js-categories .tec--badge::text"
            ).getall()

            page_details = {
                "url": url,
                "title": title,
                "timestamp": timestamp,
                "writer": writer,
                "shares_count": [
                    int(s) for s in shares_count.split() if s.isdigit()
                ][0]
                if shares_count != "None"
                else 0,
                "comments_count": int(comments_count)
                if comments_count != "None"
                else 0,
                "summary": summary,
                "sources": sources if sources != "None" else [],
                "categories": categories if categories != "None" else [],
            }
            pages_details.append(page_details)
    return pages_details
