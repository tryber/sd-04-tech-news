import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
  try:
    sleep(delay)
    response = requests.get(url, timeout=3)
  	if response.status_code != 200:
      return ""
    return response.text
  except requests.ReadTimeout:
    return ""


def scrape(fetcher, pages=1):
    url = "https://www.tecmundo.com.br/novidades?page="
    list_news = []
    for page in range(1, pages + 1):
        selector = Selector(text=fetcher(url + str(page)))
        for news in selector.css("h3.tec--card__title"):
          url = news.css("a::attr(href)").get()
          details_url = Selector(text=fetcher(url))
          title = details_url.css("#js-article-title::text").get()
          timestamp = details_url.css("time::attr(datetime)").get()
          writer = details_url.css("a.tec--author__info__link::text").get()
          shares_count = details_url.css(".tec--toolbar__item::text").re_first(
              r"[0-9]+"
          )
          comments_count = details_url.css("#js-comments-btn::text").re_first(
              r"[0-9]+"
          )
          summary = str(
      	    details_url.css(".tec--article__body p *::text").get()
          )
          sources = details_url.css(
              ".z--mb-16 .tec--badge::text"
          ).getall()
          categories = details_url.css(
              "#js-categories .tec--badge::text"
          ).getall()

          page_details = {"url": url,
                          "title": title,
                          "timestamp": timestamp,
                          "writer": writer,
                          "shares_count": shares_count,
                          "comments_count":  int(comments_count)
                          if comments_count != "None"
                          else 0,
                          "summary": summary,
                          "sources": sources, "categories": categories
                          }

          list_news.append(page_details)
  	return list_news
