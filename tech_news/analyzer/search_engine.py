from tech_news.database import db
from datetime import datetime
import re


def search_by_title(title):
    """Seu código deve vir aqui"""
    lista_title = list(
        db.news.find({"title": re.compile(title, re.IGNORECASE)})
        )
    data = []
    for x in lista_title:
        data.append((x["title"], x["url"]))
    return data


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        if datetime.strptime(date, "%Y-%m-%d"):
            lista_data = list(
                db.news.find({"timestamp": re.compile(date, re.IGNORECASE)})
            )
            data = []

        for x in lista_data:
            data.append((x["title"], x["url"]))
        return data

    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    """Seu código deve vir aqui"""
    lista_source = list(
        db.news.find({"sources": re.compile(source, re.IGNORECASE)})
        )
    data = []

    for x in lista_source:
        data.append((x["title"], x["url"]))
    return data


def search_by_category(category):
    """Seu código deve vir aqui"""
    lista_category = list(
        db.news.find({"categories": re.compile(category, re.IGNORECASE)})
    )
    data = []

    for x in lista_category:
        data.append((x["title"], x["url"]))
    return data
