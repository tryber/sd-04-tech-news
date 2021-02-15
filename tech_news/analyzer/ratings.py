from tech_news import database


def top_5_news():
    news_found = []
    news_search = database.get_top(
        [
            {
                "$addFields": {
                    "soma": {"$add": ["$shares_count", "$comments_count"]}
                }
            },
            {"$sort": {"soma": -1, "title": 1}},
            {"$limit": 5},
        ]
    )
    if len(news_search) < 5:
        return news_search
    elif len(news_search) == 0:
        return []
    for item in news_search:
        news_found.append((item["title"], item["url"]))
    return news_found


def top_5_categories():
    news_found = []
    news_search = database.get_top(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    if len(news_search) < 5:
        return news_search
    elif len(news_search) == 0:
        return []
    for item in news_search:
        print(item)
        news_found.append(item["_id"])
    return news_found
