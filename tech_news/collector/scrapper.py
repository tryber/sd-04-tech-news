import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    response = requests.get("https://www.tecmundo.com.br/novidades", timeout=3)
    if response.status_code != "200":
        return ""
    else:
        return response.text

    time.sleep(0.5)


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
