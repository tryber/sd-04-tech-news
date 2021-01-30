from tech_news.database import search_news
import datetime


def search_by_title(title):
    result = []
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    if len(search) == 1:
        result.append((search[0]["title"], search[0]["url"]))
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
    if len(search) == 1:
        result.append((search[0]["title"], search[0]["url"]))
    return result


def search_by_category(category):
    result = []
    search = search_news({"categories": {"$regex": category, "$options": "i"}})
    if len(search) == 1:
        result.append((search[0]["title"], search[0]["url"]))
    return result
