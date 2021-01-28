from tech_news import database


def search_by_title(title):
    news_list_by_title = []
    news_tittle = database.search_news(
        {"title": {"$regex": title, "$options": "-i"}}
        )
    if len(news_tittle) == 1:
        news_list_by_title.append(
            (news_tittle[0]["title"], news_tittle[0]["url"])
            )

    return news_list_by_title
# source: https://docs.mongodb.com/manual/reference/operator/query/regex/


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
