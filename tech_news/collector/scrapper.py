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
        # print('oieeeee', news)
        news.append(
            {
                "url": url,
                "title": title.strip(),
                # "timestamp": timestamp,
            }
        )
        # pageCode = parsel.Selector(url)
        # for one_notice in pageCode.css("div"):
        #     title = one_notice.css("h1.js-article-title::text")
        #     print('YESYESYES', one_notice.css("div::text").getall())
        #     # timestamp = one_notice.css("time::attr(datetime)").get()
        # print('aqui viria o q escolhi do pageCode', pageCode)

    return news


teste = fetch_content("https://www.tecmundo.com.br/novidades")

# print(teste)

respo = scrape(teste)

print(respo)
