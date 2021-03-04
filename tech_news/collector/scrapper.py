import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        print("fetching content", url)
        response = requests.get(url, timeout=timeout)
        sleep(delay)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    base_url = "https://www.tecmundo.com.br/novidades?page="
    page_number = 1

    all_news = []

    while page_number <= pages:
        content = fetcher(f"{base_url}{page_number}")
        selector = Selector(content)
        news_container = selector.css("div.tec--list__item")
        for item in news_container:
            
