from tech_news.database import db


def filter_news(data):
    filters = []
    for data_filter in data:
        filters.append((data_filter['title'], data_filter['url']))
    return filters


def top_5_news():
    """Seu código deve vir aqui"""
    # lista as cinco notícias com a maior soma
    # de compartilhamentos e comentários do banco de dados
    top_news = list(db.news.aggregate([
        {"$addFields": {
            "sum_shares_comments": {
                "$add": ["$shares_count", "$comments_count"]}}},
        {"$sort": {"sum_shares_comments": -1, "title": 1}},
        {"$limit": 5}
    ]))
    return filter_news(top_news)


def top_5_categories():
    """Seu código deve vir aqui"""
    # lista as cinco categorias com maior ocorrência no banco de dados
    filters = []
    top_categories = list(db.news.aggregate([
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]))

    for data_filter in top_categories:
        filters.append(data_filter["_id"])
    return filters
