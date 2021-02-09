from tech_news.database import get_categories, get_top


def top_5_news():
    result = []
    getData = get_top()

    for index in getData:
        result.append((index["title"], index["url"]))

    return result


def top_5_categories():
    result = []
    getData = get_categories()

    for index in getData:
        result.append((index["_id"]))

    return result
