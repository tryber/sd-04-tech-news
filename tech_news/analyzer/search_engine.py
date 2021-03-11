import datetime
from tech_news.database import search_news


def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    results = []
    for new in data:
        results.append((new["title"], new["url"]))

    return results


def search_by_date(date):
    format = "%Y-%m-%d"
    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")

    data = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    results = []
    for new in data:
        results.append((new["title"], new["url"]))

    return results


def search_by_source(source):
    data = search_news({"sources": {"$regex": source, "$options": "i"}})
    results = []
    for new in data:
        results.append((new["title"], new["url"]))

    return results


def search_by_category(category):
    data = search_news({"categories": {"$regex": category, "$options": "i"}})
    results = []
    for new in data:
        results.append((new["title"], new["url"]))

    return results
