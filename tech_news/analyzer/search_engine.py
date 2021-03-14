from tech_news import database
from datetime import datetime


def search_by_title(title):
    vazio = []
    search = database.search_news({"title": {
        "$regex": title, "$options": "i"}})
    if len(search) == 0:
        return vazio
    return [(search[0]["title"], search[0]["url"])]


def search_by_date(date):
    try:
        if datetime.strptime(date, "%Y-%m-%d"):
            found = []
            search = database.search_news({"timestamp": {"$regex": date}})
            for dat in search:
                found.append((dat["title"], dat["url"]))
            return found
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    vazio = []
    search = database.search_news({"sources": {
        "$regex": source, "$options": "i"}})
    if len(search) == 0:
        return vazio
    return [(search[0]["title"], search[0]["url"])]


def search_by_category(category):
    vazio = []
    search = database.search_news({"categories": {
        "$regex": category, "$options": "i"}})
    if len(search) == 0:
        return vazio
    return [(search[0]["title"], search[0]["url"])]
