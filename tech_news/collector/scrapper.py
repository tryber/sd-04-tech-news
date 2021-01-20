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
    # selector = Selector(text = fetch_content("https://www.tecmundo.com.br/novidades"))
    # url = selector.css("figure.tec--card__thumb a::attr(href)").getall()
    # print(url)
