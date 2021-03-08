import requests
import time
from time import sleep

def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
     time.sleep(delay)
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()  # retorna 1 objeto HTTPError
        sleep(delay)
    except (requests.exceptions.HTTPError, requests.exceptions.ReadTimeout):
        return ""
    else:
        return resp.text
    
    '''
    resp = requests.get(url, timeout=timeout)
    if resp.status_code != 200:
        return ""
    time.sleep(delay)
    return resp.text
    '''

def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
