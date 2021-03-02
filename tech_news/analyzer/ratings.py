from tech_news.database import aggregate_news


def top_5_news():
    result = []
    search = aggregate_news(
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
    for new in search:
        result.append((new["title"], new["url"]))
    return result


def top_5_categories():
    result = []
    search = aggregate_news(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "quantity": {"$sum": 1}}},
            {"$sort": {"quantity": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )

    for news in search:
        result.append((news["_id"]))

    return result
