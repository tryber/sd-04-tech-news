from tech_news.database import search_news
import datetime


def search_by_title(title):
    getData = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(data["title"], data["url"]) for data in getData]


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return search_news({"timestamp": {"$regex": date}})
    except:
        raise ValueError("Data inválida")


def search_by_source(source):
    getData = search_news({"source": {"$regex": source, "$options": "i"}})
    return [(data["title"], data["url"]) for data in getData]


def search_by_category(category):
    data = search_news({"categories": {"$regex": category, "$options": "i"}})
    return data
