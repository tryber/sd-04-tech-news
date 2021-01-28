from tech_news.database import case_isensitive_search
from datetime import datetime


def search_by_title(title):
    return case_isensitive_search("title", title)


def search_by_source(source):
    return case_isensitive_search("sources", source)


def search_by_category(category):
    return case_isensitive_search("categories", category)


def search_by_date(date):
    try:
        if datetime.strptime(date, "%Y-%m-%d"):
            return case_isensitive_search("timestamp", date)
    except ValueError:
        raise ValueError("Data inválida")
