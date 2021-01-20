import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    time.sleep(delay)
    response = requests.get(url)
    if response.status_code != 200:
        return print('')
    else:
        print(response.status_code)  # código de status
        print(response.text)  # conteúdo recebido


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
