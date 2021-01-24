import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    print("fetching: ", url)
    try:
        response = requests.get(url, timeout=timeout)
        print("status code: ", response.status_code)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    if response.status_code != 200:
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    base_url = "https://www.tecmundo.com.br/novidades"
    page = 1
    all_news = []
    url_page = "?page="

    while page <= pages:
        selector = Selector(fetcher(base_url + url_page + str(page)))
        items = selector.css(".tec--list__item")
        for index, item in enumerate(items):
            url = item.css("h3 a::attr(href)").get()
            one_news_content = fetcher(url)
            one_news_content_selector = Selector(one_news_content)
            title = one_news_content_selector.css(
                "#js-article-title::text"
            ).get()
            writer = one_news_content_selector.css(
                ".tec--author__info__link::text"
            ).get()
            share_count = one_news_content_selector.css(
                "button::attr(data-count)"
            ).get()
            comments_count = one_news_content_selector.css(
                ".tec--btn::attr(data-count)"
            ).get()
            timestamp = one_news_content_selector.css(
                ".tec--timestamp__item time::attr(datetime)"
            ).get()
            summary = one_news_content_selector.css(
                ".tec--article__body > p::text"
            ).get()
            sources = one_news_content_selector.css(
                ".z--mb-16 > div a::text"
            ).getall()
            categories = one_news_content_selector.css(
                "#js-categories a::text"
            ).getall()
            temp_list = {
                "url": url,
                "title": title,
                "timestamp": timestamp,
                "writer": writer,
                "shares_count": int(share_count),
                "comments_count": int(comments_count),
                "summary": summary,
                "sources": sources,
                "categories": categories,
            }
            all_news.append(temp_list)
        page += 1

    return all_news
