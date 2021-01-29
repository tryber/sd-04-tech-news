import requests
from time import sleep
# from parsel import Selector

BASE_URL = "https://www.tecmundo.com.br/novidades"


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        return ""
    else:
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
