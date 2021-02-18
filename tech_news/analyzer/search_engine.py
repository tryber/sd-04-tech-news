from tech_news.database import search_news
import datetime


def filter_news(data):
    filters = []
    for data_filter in data:
        filters.append((data_filter['title'], data_filter['url']))
    return filters


def search_by_title(title):
    """Seu código deve vir aqui"""
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    return filter_news(search)


def search_by_date(date):
    """Seu código deve vir aqui"""
    # datetime
    # https://stackoverflow.com/questions/55365771/
    # python-query-by-dates-that-are-stored-as-strings-in-mongodb-collection
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        search = search_news({"timestamp": {"$regex": date, "$options": "i"}})
        return filter_news(search)
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    """Seu código deve vir aqui"""
    search = search_news({"sources": {"$regex": source, "$options": "i"}})
    return filter_news(search)


def search_by_category(category):
    """Seu código deve vir aqui"""
    search = search_news({"categories": {"$regex": category, "$options": "i"}})
    return filter_news(search)
