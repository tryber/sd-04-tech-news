from tech_news import database
from datetime import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    db_result = database.search_news({
        "title": {"$regex": title, "$options": "i"}
    })
    search_result = []
    for news in db_result:
        search_result.append((news["title"], news["url"]))
    return search_result


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        db_result = database.search_news({"timestamp": {"$regex": date}})
        search_result = []
        for news in db_result:
            search_result.append((news["title"], news["url"]))
        return search_result
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    """Seu código deve vir aqui"""
    db_result = database.search_news({
        "sources": {"$regex": source, "$options": "i"}
    })
    search_result = []
    for news in db_result:
        search_result.append((news["title"], news["url"]))
    return search_result


def search_by_category(category):
    """Seu código deve vir aqui"""
    db_result = database.search_news({
        "categories": {"$regex": category, "$options": "i"}
    })
    search_result = []
    for news in db_result:
        search_result.append((news["title"], news["url"]))
    return search_result
