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
    news_list_by_source = []
    news_source = database.search_news(
        {"source": {"$regex": source, "$options": "-i"}}
        )
    if len(news_source) == 1:
        news_list_by_source.append(
            (news_source[0]["title"], news_source[0]["url"])
            )

    return news_list_by_source


def search_by_category(category):
    news_list_by_category = []
    news_category = database.search_news(
        {"title": {"$regex": category, "$options": "-i"}}
        )
    if len(news_category) == 1:
        news_list_by_category.append(
            (news_category[0]["title"], news_category[0]["url"])
            )

    return news_list_by_category

# mongo regex source:
# https://docs.mongodb.com/manual/reference/operator/query/regex/
