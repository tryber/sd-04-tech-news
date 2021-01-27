from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    found_titles = search_news({"title": {"$regex": title, "$options": "i"}})
    if found_titles == []:
        return []
    search_title = []
    for item in found_titles:
        search_title.append((item["title"], item["url"]))
    return search_title


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        found_news = search_news({"timestamp": {"$regex": date}})
        if found_news == []:
            return []
        news = []
        for item in found_news:
            news.append((item["title"], item["url"]))
        return news
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    found_news = search_news({"sources": {"$regex": source, "$options": "i"}})
    if found_news == []:
        return []
    search_title = []
    for item in found_news:
        search_title.append((item["title"], item["url"]))
    return search_title


def search_by_category(category):
    found_news = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    if found_news == []:
        return []
    search_title = []
    for item in found_news:
        search_title.append((item["title"], item["url"]))
    return search_title
