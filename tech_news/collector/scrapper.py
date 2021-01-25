import requests
import time
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    time.sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # retorna 1 objeto HTTPError
        sleep(delay)
    except (requests.exceptions.HTTPError, requests.exceptions.ReadTimeout):
        return ""
    else:
        return response.text
    '''
    response = requests.get(url, timeout=timeout)
    if response.status_code != 200:
        return ''
    time.sleep(delay)
    return response.text
    '''


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
