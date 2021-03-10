from pymongo import MongoClient
client = MongoClient()


def find_news():
    db = client.tech_news
    data = db.news.find({}, {"_id": 0})
    return data


def search_by_title(title):
    data = find_news()
    results = []
    for new in data:
        if title.lower() in new["title"].lower():
            results.append((new["title"], new["url"]))

    return results


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
