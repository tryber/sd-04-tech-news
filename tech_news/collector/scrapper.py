import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    print(requests.codes.ok)
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        response = ""
        return response
    if response.status_code != requests.codes.ok:
        response = ""
        return response
    return response.text


URL = 'https://www.tecmundo.com.br/novidades'


def scrape(fetcher, pages=1):
    articlesList = []
    for page in range(1, pages + 1):
        responseText = fetcher(f"{URL}?page={page}")
        selector = Selector(text=responseText)
        selectorLinks = selector.css(
            '.tec--list__item .tec--card__title__link::attr(href)').getall()
        for link in selectorLinks:
            articleDic = {}
            articleDic["url"] = link
            responseText1 = fetcher(link)
            selector = Selector(text=responseText1)
            articleDic["title"] = selector.css('#js-article-title::text').get()
            articleDic["timestamp"] = selector.css(
                '#js-article-date::attr(datetime)').get()
            articleDic["writer"] = selector.css('.z--font-bold a::text').get()
            articleDic["shares_count"] = selector.css(
                '#js-author-bar .tec--toolbar__item::text').get()
            if articleDic["shares_count"]:
                articleDic["shares_count"] = int(
                    articleDic["shares_count"].split()[0])
            articleDic["comments_count"] = int(selector.css(
                '#js-comments-btn::attr(data-count)').get())
            articleDic["summary"] = selector.css(
                '.tec--article__body p:first-of-type::text').get()
            articleDic["sources"] = selector.css(
                '.z--mb-16 .tec--badge::text').getall()
            articleDic["categories"] = selector.css(
                '#js-categories a::text').getall()
            articlesList.append(articleDic)
    return articlesList

# scrape(fetch_content)


# summary
