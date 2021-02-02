from tech_news.database import search_news


def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    return data


def search_by_date(date):
    data = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    return data


def search_by_source(source):
    data = search_news({"source": {"$regex": source, "$options": "i"}})
    return data


def search_by_category(category):
    data = search_news({"categories": {"$regex": category, "$options": "i"}})
    return data
