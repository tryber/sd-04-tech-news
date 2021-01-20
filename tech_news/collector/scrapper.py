import requests
import time


def fetch_content(url, timeout=3, delay=0.5):

    print(timeout)
    for _ in range(15):
        response = requests.get(url, timeout=timeout)
        print(response)
        time.sleep(delay)


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""

fetch_content("http://www.google.com")