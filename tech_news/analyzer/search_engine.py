from tech_news.database import search_news
import datetime


def general_search(field, query):
    result = search_news({field: query})
    return [(news["title"], news["url"]) for news in result]


def search_by_title(title):
    data = general_search("title", title)
    if data == []:
        return []
    return data


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        data = general_search("timestamp", date)
        return data
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
