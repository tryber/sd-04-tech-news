from tech_news.database import search_news_agregate


def create_lists(data):
    if data == []:
        return []
    search_for_news = []
    for new in data:
        search_for_news.append((new["title"], new["url"]))
    return search_for_news


def top_5_news():
    news = search_news_agregate(
        [
            {
                "$addFields": {
                    "popularity": {"$add:"["$shares_count", "$comments_count"]}
                }
            },
            {"$sort": {"popularity": -1, "title": 1}},
            {"$limit": 5},
        ]
    )
    return create_lists(news)


def top_5_categories():
    """Seu código deve vir aqui"""
