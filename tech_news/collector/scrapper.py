import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    tech_news = []
    for page in range(pages):
        URL = f"https://www.tecmundo.com.br/novidades?page={page}"
        response = fetcher(URL)
        site = Selector(text=response)
        news = site.css("h3 a.tec--card__title__link::attr(href)").getall()
        for notice in news:
            result = Selector(text=fetcher(notice))
            title = result.css("h1#js-article-title::text").get()
            timestamp = result.css(
                "time#js-article-date::attr(datetime)"
            ).get()
            writer = result.css("a.tec--author__info__link::text").get()
            shares_count = result.css("div.tec--toolbar__item::text").re_first(
                "\\d"
            )
            comments_count = result.css(
                "#js-comments-btn::attr(datacount"
            ).get()
            summary = result.css("div.tec--article__body p *::text").get()
            sources = result.css("div.z--mb-16 .tec--badge::text").getall()
            categories = result.css(
                "div#js-categories .tec--badge--primary::text"
            ).getall()
            tech_news.append(
                {
                    "url": notice,
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

    return tech_news
