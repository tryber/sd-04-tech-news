import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    time.sleep(delay)
    response = requests.get(url, timeout=timeout)
    if response.status_code == 200:
        return response.text
    return ""


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
