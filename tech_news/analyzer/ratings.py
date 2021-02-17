from tech_news.database import db


def make_tuple(data):
    new_tuple = []
    for news in data:
        new_tuple.append((news["title"], news["url"]))
    return new_tuple


def top_5_news():
    result = list(
        db.news.aggregate(
            [
                {
                    "$addFields": {
                        "sum_shares_comments": {
                            "$add": ["$shares_count", "$comments_count"]
                        }
                    }
                },
                {"$sort": {"sum_shares_comments": -1, "title": 1}},
                {"$limit": 5},
            ]
        )
    )
    return make_tuple(result)


def top_5_categories():
    result = list(
        db.news.aggregate(
            [
                {"$unwind": "$categories"},
                {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
                {"$sort": {"count": -1, "_id": 1}},
                {"$limit": 5},
            ]
        )
    )

    new_list = []
    for categorie in result:
        new_list.append(categorie["_id"])

    return new_list


# Teste local
# python3 -i tech_news/analyzer/ratings.py
# top_5_news()
# top_5_categories()
