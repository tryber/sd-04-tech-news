import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        sleep(delay)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return ""
    except requests.ReadTimeout:
        return ""


def scrape(fetcher, pages=1):
    URLBASE = "https://www.tecmundo.com.br/novidades"
    next_page = '?page=2'
    res = fetch_content(URLBASE + next_page)
    # selector = Selector(text=res.text)
    # url = selector.css("figure.tec--card__Thumb a::attr(href)").getall()
    print(res)
