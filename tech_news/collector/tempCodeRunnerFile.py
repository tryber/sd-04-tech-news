def scrape(fetcher, pages=1):
    URL = "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
    result = []

    for page in range(1, pages):
        print(page)


    response = requests.get(fetcher)
    selector = Selector(text=response.text)
    print(selector)
    title = selector.css(".tec--article__header__title::text").get()
    author = selector.css(".tec--author__info__link::text").get()
    print(title, author)


scrape("https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm")
