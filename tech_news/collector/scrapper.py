import requests
import time

def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout)
    except (response.ReadTimeout or response.status_code != 200):
        return ''
    else:
        time.sleep(delay)
        return response.text

def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
