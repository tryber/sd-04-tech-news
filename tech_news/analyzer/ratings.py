from tech_news.database import db
from bson.son import SON
import pymongo


def top_5_news():
    top_5_news_list = (
        db.news.find({})
        .sort(
            [
                ("shares_count", pymongo.DESCENDING),
                ("comments_count", pymongo.DESCENDING),
                ("title", pymongo.ASCENDING),
            ]
        )
        .limit(5)
    )
    return [(new["title"], new["url"]) for new in top_5_news_list]


def top_5_categories():
    top_5_categories_list = db.news.aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": SON([("count", 1), ("_id", 1)])},
            {"$limit": 5},
        ]
    )
    return [(new["_id"]) for new in top_5_categories_list]
