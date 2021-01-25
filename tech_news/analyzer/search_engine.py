import datetime
from ..database import search_news


def search_by(key, query):
    data = search_news({key: query})
    return [(news["title"], news["url"]) for news in data]


def search_by_title(title):
    return search_by("title", title)


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return search_by("timestamp", {"$regex": date})
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    return search_by("sources", source)


def search_by_category(category):
    return search_by("categories", category)
