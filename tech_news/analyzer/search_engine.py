from tech_news.database import search_news
import datetime


def search_by_title(title):
    getNews = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in getNews]


def search_by_date(date):
    try:
        # https://docs.python.org/pt-br/3/library/datetime.html
        datetime.datetime.strptime(date, "%Y-%m-%d")
        getNews = search_news({"timestamp": {"$regex": date}})
        return [(news["title"], news["url"]) for news in getNews]

    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    try:
        getNews = search_news({"sources": {"$regex": source, "$options": "i"}})
        return [(news["title"], news["url"]) for news in getNews]
    except ValueError:
        return []


def search_by_category(category):
    try:
        getNews = search_news(
            {"categories": {"$regex": category, "$options": "i"}}
        )
        return [(news["title"], news["url"]) for news in getNews]
    except ValueError:
        return []
