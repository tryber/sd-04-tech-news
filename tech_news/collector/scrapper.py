import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    if response.status_code != 200:
        return ""
    return response.text


def scrape(fetcher, pages=1):
    news = []
    for page in range(pages):
        base_url = "https://www.tecmundo.com.br/novidades?page=" + str(
            page + 1
        )
        print(base_url)
        selector = Selector(fetcher(base_url))
        articles = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()

        for url in articles:
            selector = Selector(fetcher(url))
            # title
            title = selector.css("#js-article-title::text").get()
            # timestamp
            timestamp = selector.css("#js-article-date::attr(datetime)").get()
            # writer
            writer = selector.css(".tec--author__info__link::text").get()
            # share_count
            shares_count = int(
                selector.css(".tec--toolbar__item::text").get().split()[0]
            )
            # comments_count
            comments_count = int(
                selector.css("#js-comments-btn::attr(data-count)").get()
            )
            # summary
            summary = "".join(
                selector.css(
                    ".tec--article__body p:first-of-type ::text"
                ).getall()
            )
            # sources
            sources = selector.css("div.z--mb-16 .tec--badge::text").getall()
            # categories
            categories = selector.css("#js-categories a::text").getall()
            # append to list
            news.append(
                {
                    "url": url,
                    "title": title,
                    "timestamp": timestamp,
                    "writer": writer,
                    "shares_count": shares_count,
                    "comments_count": comments_count,
                    "summary": summary,
                    "sources": sources,
                    "categories": categories,
                }
            )
    return news


# response = requests.get(
#     "https://www.tecmundo.com.br/mercado/210534-internet-via-satelite-elon-musk-tem-10-mil-usuarios.htm/"
# )
# selector = Selector(text=response.text)

# # O título está no atributo title em um elemento âncora (<a>)
# # Dentro de um h3 em elementos que possuem classe product_pod
# titles = "".join(
#     selector.css(".tec--article__body p:first-of-type ::text").getall()
# )
# print(titles)
# # # Estamos utilizando a::attr(title) para capturar somente o valor contido no texto do seletor

# # # Os preços estão no texto de uma classe price_color
# # # Que se encontra dentro da classe .product_price
# # prices = selector.css(".product_price .price_color::text").getall()
# # print(prices)

# # # Combinando tudo podemos buscar os produtos
# # # em em seguida buscar os valores individualmente
# # for product in selector.css(".product_pod"):
# #     title = product.css("h3 a::attr(title)").get()
# #     price = product.css(".price_color::text").get()
# #     print(title, price)
