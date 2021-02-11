from tech_news.database import search_news


def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    if data == []:
        return []
    return [(news["title"], news["url"]) for news in data]


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
