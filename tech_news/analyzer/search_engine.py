from tech_news.database import search_news
import datetime


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "-i"}})
    if len(news) == 0:
        return news

    return [(news[0]["title"], news[0]["url"])]


def search_by_date(date):
    try:
        new_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        print(new_date)
        news = search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        if len(news) == 0:
            return news
        return [(news[0]["title"], news[0]["url"])]


def search_by_source(source):
    news = search_news({"sources": {"$regex": source, "$options": "-i"}})

    if len(news) == 0:
        return news

    return [(news[0]["title"], news[0]["url"])]


def search_by_category(category):
    """Seu código deve vir aqui"""
