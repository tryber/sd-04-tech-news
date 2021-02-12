import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        response = ""
        return response
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
    news = []
    base_url = "https://www.tecmundo.com.br/novidades?page=" 
    response = fetcher(f"{base_url}{pages}")
    print("\nRESPONSE:", response)
    selector = Selector(text=response)
    url = selector.css(".tec--card__title a::attr(href)").getall()
    title = selector.css(".tec--card__title a::text").getall()
    #timestamp = selector.css("").getall()
    print("\nURL:", url[0])
    print("\nTITLE:", title[0])
    print("\nTIMESTAMP:", title[0])

    # news.append(new)
    # url = selector.css(".tec--list").getall()
    print("\nSELECTOR:", selector)
    # print(url)
    return selector


# Teste Local
# python3 -i tech_news/collector/scrapper.py
# scrape(fetcher=fetch_content, pages=2)
