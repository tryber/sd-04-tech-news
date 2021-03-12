from tech_news.analyzer.search_engine import convert_to_tuples
from tech_news.database import search_news_with_agregations


def top_5_news():
    news = search_news_with_agregations(
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
    """Seu código deve vir aqui"""
