from tech_news.database import db
import pymongo


# https://stackoverflow.com/questions/8109122/how-to-sort-mongodb-with-pymongo


def top_5_news():
    """Seu código deve vir aqui"""
    lista = (
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

    data = []
    for x in lista:
        data.append((x["title"], x["url"]))
    return data


def top_5_categories():
    """Seu código deve vir aqui"""
    data = db.news.aggregate([
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
        {"$sort": {"total": -1, "_id": 1}},
        {"$limit": 5}
    ])

    result = [x["_id"] for x in data]
    return result
    