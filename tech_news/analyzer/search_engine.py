from tech_news.database import db
from datetime import datetime


def search_by_title(title):
    data = db.news.find({"title": title.capitalize()})

    news_data = []
    for i in data:
        news_data.append((i["title"], i["url"]))

    return news_data


def search_by_date(date):
    try:
        if datetime.strptime(date, "%Y-%m-%d"):
            data = db.news.find({"timestamp": {"$regex": date}})
            news_data = []
            for i in data:
                news_data.append((i["title"], i["url"]))

        return news_data
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
