import requests
from parsel import Selector
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    response = requests.get(url)
    sleep(delay)
    if response.status_code != 200:
        return ""
    else:
        selector = Selector(text=response.text)
        print(selector)


# def scrape(fetcher, pages=1):
