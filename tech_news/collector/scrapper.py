import requests
import time
from parsel import Selector


def sleep(secs):
    time.sleep(secs)


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ''
    else:
        return response.text
    finally:
        sleep(0.5)


def scrape(fetcher=fetch_content, pages=1):
    base_url = "https://www.tecmundo.com.br/novidades"
    # Raspagem default (apenas primeira página)
    res = fetcher(base_url)
    selector = Selector(text=res)
    links = selector.css(".tec--card__info h3 a::attr(href)").getall()
    news = []
    # Extrair os detalhes de cada notícia
    for link in links:
        detail_news = fetcher(link)
        selector = Selector(text=detail_news)
        title = selector.css("#js-article-title *::text").get()
        timestamp = selector.css("#js-article-date::attr(datetime)").get()
        writer = selector.css(".tec--author__info__link::text").get()
        shares = selector.css(".tec--toolbar__item *::text").get()
        comments = selector.css("#js-comments-btn::attr(data-count)").get()
        summary = selector.css(".tec--article__body.z--px-16 *::text").get()
        sources = selector.css(".z--mb-16.z--px-16 a::text").getall()
        categories = selector.css("#js-categories a::text").getall()

        news.append({
            "url": link,
            "title": title,
            "timestamp": timestamp,
            "writer": writer,
            "shares_count": int(shares.split()[0]),
            "comments_count": int(comments),
            "summary": summary,
            "sources": list(filter(None, sources)),
            "categories": list(filter(None, categories)),
        })
    return news
