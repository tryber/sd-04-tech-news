from tech_news.database import db
from datetime import datetime
import re


def search_by_title(title):
    """Seu código deve vir aqui"""
    lista = list(db.news.find({"title": re.compile(title, re.IGNORECASE)}))
    data = []
    for x in lista:
        data.append((x["title"], x["url"]))
    return data


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        if datetime.strptime(date, "%Y-%m-%d"):
            lista = list(
                db.news.find({"timestamp": re.compile(date, re.IGNORECASE)})
            )
            data = []

        for x in lista:
            data.append((x["title"], x["url"]))
        return data

    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    """Seu código deve vir aqui"""
    lista = list(db.news.find({"sources": re.compile(source, re.IGNORECASE)}))
    data = []

    for x in lista:
        data.append((x["title"], x["url"]))
    return data


def search_by_category(category):
    """Seu código deve vir aqui"""
