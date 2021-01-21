import requests
from parsel import Selector

BASE_URL = "https://www.tecmundo.com.br/novidades/"

response = requests.get(BASE_URL + "?page=1")
selector = Selector(text=response.text)

href = selector.css(".tec--list__item h3 a::attr(href)").get()
detail_page_url = BASE_URL + href

detail_response = requests.get(detail_page_url)
detail_selector = Selector(text=detail_response.text)

description = detail_selector.css(".tec--article__header__title::text").get()
print(description)

# print(BASE_URL + href)