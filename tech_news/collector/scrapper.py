from parsel import Selector
import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        time.sleep(delay)
        return response.text
    except (requests.ReadTimeout, requests.exceptions.HTTPError):
        return ""


def scrape(fetcher, pages=1):
    base_URL = "https://www.tecmundo.com.br/novidades?page="
    scrape_list = []
    # print(fetcher("https://www.tecmundo.com.br/novidades"))

    # for p in range(1, pages + 1):
    #     selector = Selector(text=fetcher(base_URL + str(p)))
    #     url_list = selector.css(
    #         "h3.tec--card__title > a.tec--card__title__link::attr(href)"
    #     ).getall()
    #     scrape_list.extend({"url": url} for url in url_list)

    # def extractNumber(string):
    #     return [int(i) for i in string.split() if i.isdigit()][0]

    # for scrape in scrape_list:
    #     fetched = fetcher(scrape["url"])
    #     selector = Selector(text=fetched)

    #     scrape["title"] = selector.css("#js-article-title::text").get()

    #     scrape["timestamp"] = selector.css(
    #         "#js-article-date::attr(datetime)"
    #     ).get()

    #     scrape["writer"] = selector.css(
    #         "a.tec--author__info__link::text"
    #     ).get()

    #     scrape["shares_count"] = extractNumber(
    #         selector.css("div.tec--toolbar__item::text").get()
    #     )

    #     scrape["comments_count"] = extractNumber(
    #         selector.css(
    #             "div.tec--toolbar__item > button::attr(data-count)"
    #         ).get()
    #     )

    #     scrape["summary"] = selector.css(
    #         "div.tec--article__body > p::text"
    #     ).get()

    #     scrape["sources"] = selector.css(
    #         "a[class='tec--badge']::text"
    #     ).getall()

    #     scrape["categories"] = selector.css(
    #         "a.tec--badge--primary::text"
    #     ).getall()
    #     print(scrape)

    # return scrape_list


# scrape(fetch_content)
# r = fetch_content(
#   'https://www.tecmundo.com.br/minha-serie/209754-riverdale-saiba-tudo-estreia-5-temporada-recap.htm'
# )
# print(r)
