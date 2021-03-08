from tech_news.database import search_news
import re


def search_by_title(title):
    result = []
    search_result = search_news(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    )
    
    for news in search_result:
        result.append((news["title"], news["url"]))
    return result

def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
