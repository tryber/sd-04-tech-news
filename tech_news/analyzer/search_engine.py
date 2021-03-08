from tech_news.database import search_news
import re
from datetime import datetime


def search_by_title(title):
    result = []
    search_result = search_news(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    )

    for news in search_result:
        result.append((news["title"], news["url"]))
    return result


def search_by_date(date):
    result = []
    search_result = search_news({"timestamp": {"$regex": date}})
    try:
        datetime.strptime(date, "%Y-%m-%d")

        for news in search_result:
            result.append((news["title"], news["url"]))
    except ValueError:
        raise ValueError("Data inválida")    
    else:
        return result


def search_by_source(source):
    result = []
    search_result = search_news(
        {"sources": {"$all": [re.compile(source, re.IGNORECASE)]}}
    )

    for news in search_result:
        result.append((news["title"], news["url"]))
    return result


def search_by_category(category):
    result = []
    search_result = search_news({"categories": {"$all": [re.compile(category, re.IGNORECASE)]}})

    for news in search_result:
        result.append((news["title"], news["url"]))
    return result

