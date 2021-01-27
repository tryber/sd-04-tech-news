from tech_news.database import db


def search_by_title(title):
    title = title.capitalize()
    data = db.news.find({"title": title})

    news_data = []
    for i in data:
        news_data.append((i['title'], i['url']))

    return news_data


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
