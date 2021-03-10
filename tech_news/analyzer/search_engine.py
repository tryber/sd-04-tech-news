from tech_news.database import search_news


def search_by_title(title):
    new_list = []
    info = search_news({"title": {"$regex": title, "$options": "i"}})
    for new in info:
        new_list.append((new["title"], new["url"]))
    return new_list


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
