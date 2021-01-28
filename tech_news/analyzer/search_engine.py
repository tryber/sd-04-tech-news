from tech_news import database
import datetime


def search_by_title(title):
    news = database.search_news({"title": {"$regex": title, "$options": "-i"}})
    if len(news) == 0:
        return news

    return [(news[0]["title"], news[0]["url"])]


def search_by_date(date):
    try:
        newDate = datetime.datetime.strptime(date, "%Y-%m-%d")
        print(newDate)
        news = database.search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        if len(news) == 0:
            return news
        return [(news[0]["title"], news[0]["url"])]

    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
