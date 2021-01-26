from tech_news.database import search_5_categories


def top_5_news():
    """Seu código deve vir aqui"""


def top_5_categories():
    top_categories = []
    search_query = search_5_categories(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": {"_id": 1}},
            {"$limit": 5},
        ]
    )
    for cat in search_query:
        top_categories.append((cat["_id"]))
    return top_categories
