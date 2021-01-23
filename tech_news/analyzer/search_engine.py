# stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile
# stackoverflow.com/questions/9978534/match-dates-using-python-regular-expressions

from tech_news.database import search_news
import re
import datetime


def find_news_func(param, result):
    regex = re.compile(param, re.IGNORECASE)
    results_list = []
    news = search_news({result: {"$regex": regex}})
    for new in news:
        results_list.append((new["title"], new["url"]))

    return results_list


def search_by_title(title):
    return find_news_func(title, "title")


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        regex = re.compile(date, re.IGNORECASE)
        results_list = []
        news = search_news({"timestamp": regex})
        for new in news:
            results_list.append((new["title"], new["url"]))
    except ValueError:
        raise ValueError("Data inválida")
    else:
        return results_list


def search_by_source(source):
    return find_news_func(source, "sources")


def search_by_category(category):
    return find_news_func(category, "categories")
