import requests
import time


def sleep(secs):
    time.sleep(secs)


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ''
    else:
        return response.text
    finally:
        sleep(0.5)


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
