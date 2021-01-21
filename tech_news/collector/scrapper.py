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
    try:
        url = "https://www.tecmundo.com.br/produto/209717-xiaomi-lanca-robo-varre-passa-pano-r-3-679-99-brasil.htm"
        response = requests.get(url)
        selector = Selector(text=response.text)

        title = selector.css(".tec--article__header__title::text").get()
        timestamp = selector.css(
            ".tec--timestamp__item time::attr(datetime)"
        ).get()
        writer = selector.css(".tec--author__info__link::text").get()
        shares_count = (
            selector.css(".tec--toolbar__item::text")
            .get()
            .replace(" Compartilharam", "")
        )
        comments_count = selector.css(
            ".tec--toolbar__item button::attr(data-count)"
        ).get()

        summary_list = selector.css(".tec--article__body p *::text").getall()
        for i in summary_list:
            summary += i

        categories = selector.css("#js-categories .tec--badge::text").getall()

        sources_list = selector.css(".z--mb-16 div *::text").getall()
        for i in sources_list:
            if i != " ":
                sources.append(i)
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

        print(noticie)

    finally:
        return ""


scrape("a")
