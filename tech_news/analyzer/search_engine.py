from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    search_title = []
    title = search_news({"title": {"$regex": title, "$options": "i"}})
    if len(title) == 1:
        search_title.append((title[0]["title"], title[0]["url"]))
    return search_title


def search_by_date(date):
    try:
        search_date = []
        datetime.strptime(date, "%Y-%m-%d")
        date = search_news({"timestamp": {"$regex": date}})
        if len(date) == 1:
            search_date.append((date[0]["title"], date[0]["url"]))
        return search_date
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    search_source = []
    source = search_news({"sources": {"$regex": source, "$options": "i"}})
    if len(source) == 1:
        search_source.append((source[0]["title"], source[0]["url"]))
    return search_source


def search_by_category(category):
    search_category = []
    category = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    if len(category) == 1:
        search_category.append((category[0]["title"], category[0]["url"]))
    return search_category
