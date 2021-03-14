import pymongo
from tech_news.database import db


def top_5_news():
    data = (
        db.news.find({}).sort([
                ("shares_count", pymongo.DESCENDING),
                ("comments_count", pymongo.DESCENDING),
                ("title", pymongo.ASCENDING),
            ]
        ).limit(5)
    )

    news_data = []
    for i in data:
        news_data.append((i["title"], i["url"]))
    return news_data


def top_5_categories():
    """Seu código deve vir aqui"""
