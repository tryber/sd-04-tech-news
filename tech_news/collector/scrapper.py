import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        time.sleep(delay)
        return response.text
    except requests.ReadTimeout:
        return ''


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
