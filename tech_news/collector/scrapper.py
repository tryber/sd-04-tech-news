import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    print("Fetching", url)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        sleep(delay)
    except (requests.ReadTimeout, requests.exceptions.HTTPError):
        return ""
    if (response.status_code != 200):
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
