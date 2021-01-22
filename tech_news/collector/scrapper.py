import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
        response.raise_for_status()
    except requests.ReadTimeout:
        return ""
    except requests.HTTPError:
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    summary = ""
    sources = []

    response_principal = requests.get("https://www.tecmundo.com.br/novidades")

    selector_principal = Selector(text=response_principal.text)

    list_noticies_URL = selector_principal.css(
        ".tec--card__title a::attr(href)"
    ).getall()

    for i in list_noticies_URL:
        url = i
        response = requests.get(url)
        selector = Selector(text=response.text)

        title = selector.css(".tec--article__header__title::text").get()
        timestamp = selector.css(
            ".tec--timestamp__item time::attr(datetime)"
        ).get()
        writer = selector.css(".tec--author__info__link::text").get()
        if writer is None:
            writer = selector.css(
                ".z--items-center .tec--timestamp  .z--font-bold a::text"
            ).get()

        shares_count = (
            selector.css(".tec--toolbar__item::text")
            .get()
            .replace(" Compartilharam", "")
        )
        if shares_count is None:
            shares_count = 0

        comments_count = selector.css(
            ".tec--toolbar__item button::attr(data-count)"
        ).get()

        summary_list = selector.css(".tec--article__body *::text").getall()
        for i in summary_list:
            summary += i

        categories = selector.css("#js-categories .tec--badge::text").getall()

        sources_list = selector.css(".z--mb-16 div *::text").getall()
        for i in sources_list:
            if i != " ":
                sources.append(i)
        noticies = []
        noticie = {
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
        noticies.append(noticie)
        # print(noticie)
        return noticies
