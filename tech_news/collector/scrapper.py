import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        sleep(delay)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return ""
        return response.text
    except requests.ReadTimeout:
        return ""


def scrape(fetcher, pages=1):
    url = "https://www.tecmundo.com.br/novidades?page="
    list_news = []
    for page in range(1, pages + 1):
        selector = Selector(text=fetcher(url + str(page)))
        for news in selector.css("h3.tec--card__title"):
            url = news.css("a::attr(href)").get()
            details_url = Selector(text=fetcher(url))
            title = details_url.css("#js-article-title::text").get()
            timestamp = details_url.css("time::attr(datetime)").get()
            writer = details_url.css(".z--m-none strong").get()
            page_details = {"url": url, "title": title,
                            "timestamp": timestamp, "writer": writer}

            list_news.append(page_details)
    print(list_news)
