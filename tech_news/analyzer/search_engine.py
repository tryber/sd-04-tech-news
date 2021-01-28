from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    result = []
    db_result = search_news({"title": {"$regex": title, "$options": "i"}})

    if len(db_result) == 1:
        result.append((db_result[0]["title"], db_result[0]["url"]))

    return result


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        result = []
        datetime.strptime(date, "%Y-%m-%d")
        date = search_news({"timestamp": {"$regex": date}})

        if len(date) == 1:
            result.append((date[0]["title"], date[0]["url"]))

        return result
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    """Seu código deve vir aqui"""
    result = []
    source = search_news({"sources": {"$regex": source, "$options": "i"}})

    if len(source) == 1:
        result.append((source[0]["title"], source[0]["url"]))

    return result


def search_by_category(category):
    """Seu código deve vir aqui"""
    result = []
    category = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )

    if len(category) == 1:
        result.append((category[0]["title"], category[0]["url"]))

    return result
