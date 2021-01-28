from ..database import get_top5

def top_5_news():
    result = get_top5()
    return [(news["title"], news["url"]) for news in result]


def top_5_categories():
    """Seu código deve vir aqui"""
