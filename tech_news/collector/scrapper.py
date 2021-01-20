import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
        print(response.status_code)
    except requests.ReadTimeout:
        return ""
    if response.status_code != 200:
        print("inside code != 200")
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
