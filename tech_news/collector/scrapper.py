import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    if response.status_code != 200:
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    selector = Selector(fetcher)
    items = selector.css(".tec--list__item").getall()
    print("items :", items)

    # for item in selector.css(".tec--list__item"):
    for index, item in enumerate(selector.css(".tec--list__item")):
        title = item.css(".tec--card__title__link::text").get()
        print("index", index)
        print(title)

    return 2
