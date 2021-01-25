from tech_news.database import search_news_with_agregations
from tech_news.analyzer.search_engine import format_tuples


def top_5_news():
    news_data = search_news_with_agregations(
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
    print(news_data)
    return format_tuples(news_data)


def top_5_categories():
    news_categories = []
    news_data = search_news_with_agregations(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    for news in news_data:
        news_categories.append((news["_id"]))
    return news_categories
