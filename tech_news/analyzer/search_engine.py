from tech_news.database import search_news
from datetime import datetime


def convert_to_tuples(data):
    if data == []:
        return []
    news_container = []
    for news in news_container:
        news_container.append((news["title"], news["url"]))
    return news_container


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return convert_to_tuples(news)


def search_by_date(date):
    try:
        newDate = datetime.strptime(date, "%Y-%m-%d")
        print(newDate)
        news = search_news({"timestamp": {"$regex": date, "$options": "i"}})
        return convert_to_tuples(news)
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    return convert_to_tuples(news)


def search_by_category(category):
    news = search_news({"categories": {"$regex": category, "$options": "i"}})
    return convert_to_tuples(news)
