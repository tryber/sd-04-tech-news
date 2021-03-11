import requests


def fetch_content(url, timeout=3, delay=0.5):
    data = requests.get(url)
    if (data.status_code != 200):
        return ''
    return data.content


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
