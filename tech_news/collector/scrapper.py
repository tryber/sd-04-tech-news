import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqu
    i"""
    response = requests.get(url, timeout=timeout)
    sleep(delay)
    print(response.text)
    return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""


fetch_content('https://g1.globo.com')