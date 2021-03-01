import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    print("Fetching", url)
    try:
        response = requests.get(url, timeout=timeout)
        print(response.status_code)
        sleep(delay)
    except response.HTTPError:
        return ""
    if (response.status_code != 200):
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    # url = "https://www.tecmundo.com.br/novidades"
