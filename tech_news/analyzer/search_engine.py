import datetime
from tech_news import database


def search_by_title(title):
    news_found = []
    news_search = database.search_news({
        "title": {"$regex": title, "$options": "i"}
    })
    if len(news_search) == 0:
        return []
    for item in news_search:
        news_found.append((item["title"], item["url"]))
    return news_found


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        news_found = []
        news_search = database.search_news({
            "timestamp": {"$regex": date, "$options": "i"}
        })
        if len(news_search) == 0:
            return []
        for item in news_search:
            news_found.append((item["title"], item["url"]))
        return news_found
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    news_found = []
    news_search = database.search_news({
        "sources": {"$regex": source, "$options": "i"}
    })
    if len(news_search) == 0:
        return []
    for item in news_search:
        news_found.append((item["title"], item["url"]))
    return news_found


def search_by_category(category):
    news_found = []
    news_search = database.search_news({
        "categories": {"$regex": category, "$options": "i"}
    })
    if len(news_search) == 0:
        return []
    for item in news_search:
        news_found.append((item["title"], item["url"]))
    return news_found
