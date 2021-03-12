from tech_news.analyzer.search_engine import convert_to_tuples
from tech_news.database import search_news_agrregations


def top_5_news():
    news = search_news_agrregations(
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
    # print(news)
    return convert_to_tuples(news)


def top_5_categories():
    categories = []
    data = search_news_agrregations(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    for news in data:
        categories.append((news["_id"]))
    return categories
