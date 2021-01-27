from tech_news import database


def search_by_title(title):
    results = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    if results == []:
        return []
    news = []
    for item in results:
        news.append((item["title"], item["url"]))
    return news


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
