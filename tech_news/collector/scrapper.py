import requests
import parsel
from time import sleep


URL = "https://www.tecmundo.com.br/novidades?page="


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except (requests.HTTPError, requests.exceptions.ReadTimeout):
        return ""
    else:
        return response.text


def extract_scrapes(select, url):
    selector = select
    title_found = selector.css(".tec--article__header__title::text").get()
    time_found = selector.css("#js-article-date::attr(datetime)").get()
    writer_found = selector.css("a.tec--author__info__link::text").get()
    share_found = selector.css(".tec--toolbar__item::text").re_first(r'\d')
    if share_found is None:
        share_found = 0
    comments_found = selector.css("#js-comments-btn::attr(data-count)").get()
    summary_found = selector.css(".tec--article__body p::text").extract_first()
    sources_found = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories_found = selector.css("#js-categories a::text").getall()
    scrapes = {
        "url": url,
        "title": title_found,
        "timestamp": time_found,
        "writer": writer_found,
        "shares_count": int(share_found),
        "comments_count": int(comments_found),
        "summary": summary_found,
        "sources": sources_found,
        "categories": categories_found,
    }
    return scrapes


def contents(urls, fetcher):
    content = []
    for url in urls:
        page = fetcher(url)
        selector = parsel.Selector(page)
        content.append(extract_scrapes(selector, url))
    return content


def scrape(fetcher, pages=1):
    result = []
    for page in range(1, pages + 1):
        pages_fetcher = fetcher(URL + str(page))
        pages_contents = parsel.Selector(pages_fetcher)
        all_url = pages_contents.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
            ).getall()
        result.extend(contents(all_url, fetcher))

    return result
