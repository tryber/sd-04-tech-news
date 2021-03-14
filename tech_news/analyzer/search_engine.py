from ..database import search_news


def serach_by_key(key, query):
    searched_news = search_news({key: {"$regex": query, "$options": "i"}})
    return [(new["title"], new["url"]) for new in searched_news]


def search_by_title(title):
    return serach_by_key("title", title)


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
