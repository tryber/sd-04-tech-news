from tech_news.database import search_news
import re
from datetime import datetime


def search_by_title(title):
    # https://docs.python.org/3/library/re.html
    # IGNORECASE
    result = []
    search_results = search_news(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    )

    for news in search_results:
        result.append((news["title"], news["url"]))

    # print(result)
    return result


def search_by_date(date):
    # https://docs.python.org/pt-br/3/library/datetime.html#strftime-and-strptime-behavior
    try:
        datetime.strptime(date, "%Y-%m-%d")

        result = []
        search_results = search_news({"timestamp": {"$regex": date}})
        for news in search_results:
            result.append((news["title"], news["url"]))
    except ValueError:
        raise ValueError("Data inválida")
    else:
        return result


def search_by_source(source):
    result = []
    search_results = search_news(
        {"sources": {"$all": [re.compile(source, re.IGNORECASE)]}}
    )

    for news in search_results:
        result.append((news["title"], news["url"]))

    # print(result)
    return result


def search_by_category(category):
    result = []
    search_results = search_news(
        {"categories": {"$all": [re.compile(category, re.IGNORECASE)]}}
    )

    for news in search_results:
        result.append((news["title"], news["url"]))

    # print(result)
    return result
