from tech_news.database import aggregate


def top_5_news():
    result = []

    db_result = aggregate(
        [
            {
                "$addFields": {
                    "popularity": {
                        "$add": ["$shares_count", "$comments_count"]
                    }
                }
            },
            {"$sort": {"popularity": -1, "title": 1}},
            {"$limit": 5},
        ]
    )

    result.append((db_result[0]["title"], db_result[0]["url"]))

    return result


def top_5_categories():
    categories = []
    db_result = aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": {"_id": 1}},
            {"$limit": 5},
        ]
    )

    for cat in db_result:
        categories.append((cat["_id"]))

    return categories
