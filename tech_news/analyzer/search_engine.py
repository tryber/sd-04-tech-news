from tech_news.database import search_news
import datetime


def search_by_title(title):
    result = []
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    for new in search:
        result.append((new["title"], new["url"]))
    return result


def search_by_date(date):
    try:
        results = []
        datetime.datetime.strptime(date, "%Y-%m-%d")
        search = search_news({"timestamp": {"$regex": date}})
        for new in search:
            results.append((new["title"], new["url"]))
    except ValueError:
        raise ValueError("Data inválida")
    else:
        return results


def search_by_source(source):
    result = []
    search = search_news({"sources": {"$regex": source, "$options": "i"}})
    for new in search:
        result.append((new["title"], new["url"]))
    return result


def search_by_category(category):
    result = []
    search = search_news({"categories": {"$regex": category, "$options": "i"}})
    for new in search:
        result.append((new["title"], new["url"]))
    return result
