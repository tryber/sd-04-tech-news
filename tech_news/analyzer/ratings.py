from tech_news.database import search_news_agregationsbd


def top_5_news():
    """Lsita top 5 noticias com maior compartilhamento"""
    info = search_news_agregationsbd(
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
    list_top5 = []
    if info == []:
        return []
    for new in info:
        list_top5.append((new["title"], new["url"]))
    return list_top5


def top_5_categories():
    """Lsita top 5 categorias se nao existir retorna um list vazia"""
    info = search_news_agregationsbd(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    list_top5_categories = []
    if info == []:
        return []
    for new in info:
        list_top5_categories.append((new["_id"]))
    return list_top5_categories
