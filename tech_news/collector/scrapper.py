import requests
from time import sleep

import parsel


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    selector = parsel.Selector(fetcher)
    news = []
    for notice in selector.css("div.tec--list__item"):
        url = notice.css("a.tec--card__title__link::attr(href)").get()
        title = notice.css("h3.tec--card__title *::text").get()
        pageCode = parsel.Selector(url)
        timestamp = notice.css("time::attr(datetime)").get()
        # for one_notice in pageCode:
        news.append(
            {
                "url": url,
                "title": title.strip(),
                "timestamp": timestamp,
            }
        )

    return len(news)


teste = fetch_content("https://www.tecmundo.com.br/produto/209787-microsoft-registra-tela-ajusta-angulo-visao-automaticamente.htm")

# print(teste)

respo = scrape(teste)

print(respo)
