from tech_news.database import search_news
import re
from datetime import datetime


def search_by_title(title):
    list_result = []
    info = search_news({"title": {"$regex": title, "$options": "i"}})
    for new in info:
        list_result.append((new["title"], new["url"]))
    return list_result


def search_by_date(date):
    list_result = []
    search_result = search_news({"timestamp": {"$regex": date}})
    try:
        datetime.strptime(date, "%Y-%m-%d")

        for news in search_result:
            list_result.append((news["title"], news["url"]))
    except ValueError:
        raise ValueError("Data inválida")
    else:
        return list_result


def search_by_source(source):
    list_result = []
    search_result = search_news(
        {"sources": {"$all": [re.compile(source, re.IGNORECASE)]}}
    )

    for news in search_result:
        list_result.append((news["title"], news["url"]))
    return list_result


def search_by_category(category):
    list_result = []
    search_result = search_news(
        {"categories": {"$all": [re.compile(category, re.IGNORECASE)]}}
    )

    for news in search_result:
        list_result.append((news["title"], news["url"]))
    return list_result
