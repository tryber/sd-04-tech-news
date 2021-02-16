from tech_news.database import search_news
import datetime


def make_tuple(data):
    new_tuple = []
    for news in data:
        new_tuple.append((news["title"], news["url"]))
    return new_tuple


def search_by_title(title):
    result = search_news({"title": {"$regex": title, "$options": 'im'}})
    print("\nRESULT:", result)
    return make_tuple(result)


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        result = search_news({"timestamp": {"$regex": date, "$options": 'im'}})
        return make_tuple(result)
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""


# Teste local
# python3 -i tech_news/analyzer/search_engine.py
# search_by_title("Musk")
# search_by_date("2020-11-11")
# search_by_source("Venture Beat")
# search_by_category("Tesla")
