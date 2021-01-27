from tech_news import database
import datetime


def search_by_title(title):
    results = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    if results == []:
        return []
    news = []
    for item in results:
        news.append((item["title"], item["url"]))
    return news


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        results = database.search_news({"timestamp": {"$regex": date}})
        if results == []:
            return []
        news = []
        for item in results:
            news.append((item["title"], item["url"]))
    except ValueError:
        raise ValueError("Data inválida")
    return news


def search_by_source(source):
    results = database.search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    if results == []:
        return []
    news = []
    for item in results:
        news.append((item["title"], item["url"]))
    return news


def search_by_category(category):
    results = database.search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    if results == []:
        return []
    news = []
    for item in results:
        news.append((item["title"], item["url"]))
    return news
