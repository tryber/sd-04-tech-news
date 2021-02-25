import requests
from time import sleep

# from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        response = ""
        return response
    if response.status_code != 200:
        response = ""
        return response

    return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
