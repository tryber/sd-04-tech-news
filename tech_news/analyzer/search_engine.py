from tech_news.database import search_news
import re


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
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
