import requests
import time

def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout)
    except OSError:
        print('')
    else:
        print(response.text)
    time.sleep(delay)

def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
