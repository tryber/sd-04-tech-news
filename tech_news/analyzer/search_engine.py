from tech_news.database import find_news
from datetime import datetime


def create_tuple(data):
    if data == []:
        return []
    search_for_news = []
    for news in data:
        search_for_news.append((news["title"], news["url"]))
        return search_for_news


def search_by_title(title):
    news_data = find_news({"title": {"$regex": title, "$options": "i"}})
    return create_tuple(news_data)


def search_by_date(date):
    try:
        if datetime.strptime(date, "%Y-%m-%d"):
            news_data = find_news(
                {"timestamp": {"$regex": date, "$options": "i"}}
            )
            return create_tuple(news_data)
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    news_data = find_news({"sources": {"$regex": source, "$options": "i"}})
    return create_tuple(news_data)


def search_by_category(category):
    news_data = find_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    return create_tuple(news_data)
