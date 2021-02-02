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
        	details_selector = Selector(text=fetcher(url))
            title = str(
                details_selector.css(
                    "h1.tec--article__header__title::text"
                ).get()
            )
            timestamp = str(
                details_selector.css("#js-article-date::attr(datetime)").get()
            )
            writer = str(
                details_selector.css(".tec--author__info__link::text").get()
            )
            shares_count = str(
                details_selector.css(".tec--toolbar__item::text").get()
            )
            comments_count = str(
                details_selector.css(
                    "#js-comments-btn::attr(data-count)"
                ).get()
            )
            summary = str(
                details_selector.css(".tec--article__body p *::text").get()
            )
            sources = details_selector.css(
                ".z--mb-16 .tec--badge::text"
            ).getall()
            categories = details_selector.css(
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
