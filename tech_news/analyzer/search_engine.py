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
    return general_search("sources", source)


def search_by_category(category):
    return general_search("categories", category)
