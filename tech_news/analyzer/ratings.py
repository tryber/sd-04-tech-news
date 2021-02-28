from tech_news.database import aggregate


def top_5_news():
    result = []
    db_result = aggregate(
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
    result.append((db_result[0]["title"], db_result[0]["url"]))

    return result


def top_5_categories():
    """Seu código deve vr aqui"""
