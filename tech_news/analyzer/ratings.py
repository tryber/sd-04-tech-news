from tech_news.database import get_categories, get_top5


def top_5_news():
    results = []
    noticias = get_top5()

    for noticia in noticias:
        results.append((noticia["title"], noticia["url"]))

    return results


def top_5_categories():
    results = []
    categories = get_categories()

    for cotegory in categories:
        results.append((cotegory["_id"]))

    return results
    