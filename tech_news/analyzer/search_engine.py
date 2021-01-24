# from pymongo import MongoClient
from tech_news import database


def search_by_title(title):
    output_list = []
    news = database.search_news({"title": {"$regex": title}})
    if len(news) == 1:
        output_list.append((news[0]["title"], news[0]["url"]))

    return output_list


def search_by_date(date):
    output_list = []
    news = database.search_news({"timestamp": {"$regex": date}})
    if len(news) == 1:
        output_list.append((news[0]["timestamp"], news[0]["url"]))

    return output_list


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
