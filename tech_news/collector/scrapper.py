import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        print(response)
        sleep(delay)
        print(response.status_code)

        if response.status_code != 200:
            return ""

        return response.text
    except requests.ReadTimeout:
        return ""


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
