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


def search_by_date(date):
    try:
        news_list_by_date = []
        news_date = database.search_news({"timestamp": {"$regex": date}})
        if len(news_date) == 1:
            news_list_by_date.append(
                (news_date[0]["title"], news_date[0]["url"])
                )
    except ValueError:
        raise ValueError("Data inválida")

    return news_list_by_date


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""

# mongo regex source:
# https://docs.mongodb.com/manual/reference/operator/query/regex/
