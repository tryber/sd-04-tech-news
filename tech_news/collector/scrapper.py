import time
import parsel
import requests

Url = "https://www.tecmundo.com.br/novidades"


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
        time.sleep(delay)
        print(response.status_code)
        if response.status_code == 200:
            # print(response.text)
            return response.text
    except requests.status_codes:
        requests.get(url + "/404")
        return ""


def scrape(fetcher=Url, pages=1):
    """Seu código deve vir aqui"""
    # Faz a requisição da url pagina 1
    response = requests.get(fetcher + "?page=" + str(pages))
    # contando as paginas
    list_news = []

    selector = parsel.Selector(text=response.text)
    # obtendo todos os links de notícias (href)
    response_all_link_news = \
        selector.css('.tec--card__info h3 a::attr(href)').getall()
    # print(response_all_link_news)
    # obtendo as noticias de cada link
    for link_news in response_all_link_news:
        # print(link_news)
        response_news = requests.get(link_news)
        selector = parsel.Selector(text=response_news.text)
        title = selector.css(".tec--article__header__title *::text").get()
        timestamp = selector.css("time::attr(datetime)").get()
        author = selector.css(".tec--author__info__link::text").get()
        shares_count = selector.css(".tec--toolbar__item *::text").get()
        comments_count = \
            selector.css("#js-comments-btn::attr(data-count)").get()
        summary = selector.css(".tec--article__body.z--px-16 *::text").get()
        sources = selector.css(".z--mb-16.z--px-16 a::text").getall()
        categories = selector.css("#js-categories a::text").getall()
        list_news.append({'url': link_news,
                          'title': title,
                          'timestamp': timestamp,
                          'writer': author,
                          'shares_count': shares_count,
                          'comments_count': comments_count,
                          'summary': summary,
                          'sources': list(sources),
                          'categories': list(categories)}),

    return print(list_news)
