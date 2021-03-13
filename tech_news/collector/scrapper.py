import requests
import time

def fetch_content(url, timeout=3, delay=0.5):
 try:
        response = requests.get(url, timeout=timeout)
        time.sleep(delay)
    except requests.ReadTimeout:
        return ""
    if response.status_code == 200:
        return response.text
    else:
        return ""

def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
