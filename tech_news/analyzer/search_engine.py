from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    list_result = []
    info = search_news({"title": {"$regex": title, "$options": "i"}})
    for new in info:
        list_result.append((new["title"], new["url"]))
    return list_result


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        info = search_news({"timestamp": {"$regex": date}})
        if info == []:
            return []
        list_result = []
        for new in info:
            list_result.append((new["title"], new["url"]))
        return list_result
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    list_result = []
    info = search_news({"sources": {"$regex": source, "$options": "i"}})
    if info == []:
        return []
    for new in info:
        list_result.append((new["title"], new["url"]))
    return list_result


def search_by_category(category):
    list_result = []
    info = search_news({"categories": {"$regex": category, "$options": "i"}})
    if info == []:
        return []
    for new in info:
        list_result.append((new["title"], new["url"]))
    return list_result
