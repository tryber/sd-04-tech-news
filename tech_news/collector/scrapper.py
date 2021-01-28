from parsel import Selector
import requests
import time

def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        time.sleep(delay)
        return response.text
    except (requests.ReadTimeout, requests.exceptions.HTTPError):
        return ""

def scrape(fetcher, pages=1):
    base_URL = "https://www.tecmundo.com.br/novidades?page="
    scrape_list = []

    for p in range(1, pages + 1):
        selector = Selector(text=fetcher(base_URL + str(p)))
        url_list = selector.css(
            "h3.tec--card__title > a.tec--card__title__link::attr(href)"
        ).getall()
        scrape_list.extend({"url": url} for url in url_list)

    def extractNumber(string):
        return [int(i) for i in string.split() if i.isdigit()][0]

