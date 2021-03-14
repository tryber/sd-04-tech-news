from tech_news.database import search_news


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "-i"}})
    if len(news) == 0:
        return news

    return [(news[0]["title"], news[0]["url"])]


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
