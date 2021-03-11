from tech_news.database import search_news_agregationsbd


def top_5_news():
    """Seu código deve vir aqui"""


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
