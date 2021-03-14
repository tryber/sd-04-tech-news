from tech_news.database import db
import pymongo


def top_5_news():
    top = db.news.find({}).sort(
        [
            ("shares_count", pymongo.DESCENDING),
            ("comments_count", pymongo.DESCENDING),
            ("title", pymongo.ASCENDING),
        ]).limit(5)
    result = []
    for data in top:
        result.append((data["title"], data["url"]))
    return result


def top_5_categories():
    top = db.news.aggregate([
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
        {"$sort": {"total": -1, "_id": 1}},
        {"$limit": 5},
    ])
    result = []
    for data in top:
        result.append((data["_id"]))
    return result
