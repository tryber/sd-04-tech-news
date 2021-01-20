import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
