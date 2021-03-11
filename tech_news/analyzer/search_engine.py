import datetime
from tech_news.database import search_news


def search_by_title(title):
    """Busca noticia pelo titulo se nao existir retorna uma list vazia"""
    new_list = []
    info = search_news({"title": {"$regex": title, "$options": "i"}})
    for new in info:
        new_list.append((new["title"], new["url"]))
    return new_list


def search_by_date(date):
    """Busca noticia pela data se nao existir retorna um list vazia"""
    try:
        datetime.datetime.strftime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        new_list = []
        data = search_news({"timestamp": {"$regex": date}})
        for new in data:
            new_list.append((new["title"], new["url"]))
            return new_list


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
