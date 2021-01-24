# from pymongo import MongoClient
from tech_news import database
import datetime


def search_by_title(title):
    output_list = []
    news = database.search_news({"title": {"$regex": title, "$options": "-i"}})
    if len(news) == 1:
        output_list.append((news[0]["title"], news[0]["url"]))

    return output_list


def search_by_date(date):
    try:
        newDate = datetime.datetime.strptime(date, "%Y-%m-%d")
        print(newDate)
        output_list = []
        news = database.search_news({"timestamp": {"$regex": date}})
        if len(news) == 1:
            output_list.append((news[0]["title"], news[0]["url"]))
    except ValueError:
        raise ValueError("Data inválida")

    return output_list


def search_by_source(source):
    output_list = []
    news = database.search_news({"sources": {"$regex": source, "$options": "-i"}})
    if len(news) == 1:
        output_list.append((news[0]["title"], news[0]["url"]))

    return output_list


def search_by_category(category):
    output_list = []
    news = database.search_news({"categories": {"$regex": category, "$options": "-i"}})
    if len(news) == 1:
        output_list.append((news[0]["title"], news[0]["url"]))

    return output_list
