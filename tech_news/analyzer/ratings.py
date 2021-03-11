from tech_news.database import aggregate


def top_5_news():
    data = aggregate([
        {
            "$addFields": {
                "popularity": {"$sum": ["$shares_count", "$comments_count"]}
            }
        },
        {"$sort": {"popularity": -1, "title": 1}
         },
        {"$limit": 5}
    ])

    results = []
    for new in data:
        results.append((new["title"], new["url"]))

    return results


def top_5_categories():
    data = aggregate([
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}},
        {"$limit": 5}
    ])

    results = []
    for category in data:
        results.append((category["_id"]))

    return results
