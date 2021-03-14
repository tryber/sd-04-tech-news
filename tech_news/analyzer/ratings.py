from tech_news.database import db
from pymongo import ASCENDING, DESCENDING


def top_5_news():
    data = (
        db.news.find({})
        .sort(
            [
                ("shares_count", DESCENDING),
                ("comments_count", DESCENDING),
                ("title", ASCENDING),
            ]
        ).limit(5)
    )

    news = []

    for new in data:
        news.append((new["title"], new["url"]))
    return news


def top_5_categories():
    """Seu código deve vir aqui"""
