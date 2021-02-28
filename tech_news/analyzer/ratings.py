from tech_news.database import aggregate


def top_5_news():
    result = []
    search = aggregate(
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
    """Seu código deve vr aqui"""
