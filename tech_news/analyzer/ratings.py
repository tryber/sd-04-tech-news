from tech_news.database import db
from pymongo import ASCENDING, DESCENDING
from bson.son import SON


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
    data = db.news.aggregate([
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
        {"$sort": SON([("count", 1), ("_id", 1)])},
        {"$limit": 5},
    ])

    news = []

    for new in data:
        news.append((new["_id"]))

    return news
