from tech_news.database import search_aggregator


def top_5_news():
    data = search_aggregator(
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
    return [(news["title"], news["url"]) for news in data]


def top_5_categories():
    data = search_aggregator(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
            {"$sort": {"total": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    return [(news["title"], news["url"]) for news in data]
