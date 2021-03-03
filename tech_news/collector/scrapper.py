import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    print("Fetching", url)
    try:
        response = requests.get(url, timeout=timeout)
        print(response.json())
        sleep(delay)
    except response.HTTPError:
        return ""
    if (response.status_code != 200):
        return ""
    else:
        return response.text


# def scrape(fetcher, pages=1):
#     base_url = "https://www.tecmundo.com.br/novidades"

fetch_content("https://www.tecmundo.com.br/novidades")
