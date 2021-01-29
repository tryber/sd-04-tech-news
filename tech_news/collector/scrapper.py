import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    response = requests.get(url, timeout=timeout)
    sleep(delay)
    # print('Iniciando o projeto tech-news')
    # print('response:', response)
    # print(response.status_code)
    if (response.status_code != 200):
        response = ""
        return response
    # print('headers:', response.headers["Content-Type"])
    # print('response.text:', response.text)
    return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
