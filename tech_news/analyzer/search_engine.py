from tech_news.database import search_news
from datetime import datetime

def format_tuples(news_data):
    if news_data == []:
        return []
    search_for_news = []
    for new in news_data:
        search_for_news.append((new["title"], new["url"]))
        return search_for_news

def search_by_title(title):
    news_data = search_news({"title": {"$regex": title, "$options": "i"}})
    return format_tuples(news_data)

def search_by_date(date):
    try:
        if datetime.strptime(date, "%Y-%m-%d"):
            news_data = search_news(
                {"timestamp": {"$regex": date, "$options": "i"}}
            )
            return format_tuples(news_data)
    except ValueError:
        raise ValueError("Data inválida")

def search_by_source(source):
    news_data = search_news({"sources": {"$regex": source, "$options": "i"}})
    return format_tuples(news_data)

def search_by_category(category):
    news_data = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    return format_tuples(news_data)
