from ..database import get_top5, get_top_categories


def top_5_news():
    result = get_top5()
    return [(news["title"], news["url"]) for news in result]


def top_5_categories():
    result = get_top_categories()
    return [cat["_id"] for cat in result]
