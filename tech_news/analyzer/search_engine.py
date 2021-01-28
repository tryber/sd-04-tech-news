from pymongo import MongoClient

# para testes locais com usuário e senha
client = MongoClient(
    "mongodb://root:rootteste@localhost:27017/?authMechanism=DEFAULT"
)
db = client.tech_news


def search_by_title(title):
    ar = []
    for document in db.news.find(
        {"title": {"$regex": title, "$options": "-i"}}
    ):
        title = document["title"]
        url = document["url"]
        ar.append((title, url))
    return ar


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
