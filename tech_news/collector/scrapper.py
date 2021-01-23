import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    pages_details = []
    page_url = fetcher
    for _ in range(pages):
        selector = Selector(text=page_url)
        for news in selector.css(".tec--card__title"):
            url = news.css("a::attr(href)").get()
            details_selector = Selector(text=fetch_content(url))
            page_details = {
                "url": url,
                "title": details_selector.css(
                    "h1.tec--article__header__title::text"
                ).get(),
                "timestamp": details_selector.css(
                    "#js-article-date::attr(datetime)"
                ).get(),
                "writer": details_selector.css(
                    ".tec--author__info__link::text"
                ).get(),
                "shares_count": str(
                    details_selector.css(".tec--toolbar__item::text").get()
                )[1],
                "comments_count": details_selector.css(
                    "#js-comments-btn::attr(data-count)"
                ).get(),
                "summary": details_selector.css(
                    ".tec--article__body p *::text"
                ).get(),
                "sources": details_selector.css(
                    ".z--mb-16 .tec--badge::text"
                ).getall(),
                "categories": details_selector.css(
                    "#js-categories .tec--badge::text"
                ).getall(),
            }
            pages_details.append(page_details)
        next_page_url = selector.css(".tec--btn::attr(href)").get()
        page_url = fetch_content(str(next_page_url))
        print(pages_details)


scrape(fetch_content("https://www.tecmundo.com.br/novidades"))
