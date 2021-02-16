# modulo par fazer requisicoes
# (https://www.w3schools.com/python/module_requests.asp)
import requests
# modulo time que tem varias funcoes para lidar com tempo,
# sleep funciona como setTimeOut
# (https://www.programiz.com/python-programming/time/sleep)
from time import sleep
# modulo para remover informacoes de html
# (https://parsel.readthedocs.io/en/latest/usage.html)
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    # bloco try/except = try/catch
    url = "https://www.tecmundo.com.br/novidades"
    try:
        # fazendo a requisicao http
        response = requests.get(
            url, timeout=timeout
        )
    # tratativa de erro
    # (https://requests.readthedocs.io/en/master/_modules/requests/exceptions/)
    # / erro de status_code
    except requests.ReadTimeout or response.status_code != 200:
        return ""
    else:
        # chama o delay
        sleep(delay)
        # console.log da response
        print(response)
        # retornos do resquests
        # (https://www.w3schools.com/python/ref_requests_response.asp)
        return response.text


def scrape(fetcher, pages=1):
    # url para pegar dados
    base_url = "https://www.tecmundo.com.br/novidades"
    # pagina inicial pra raspagem
    page = 1
    # lista para conter os dados extraidos
    news = []

    # estrutura de repeticao
    while page <= pages:
        # request da pag que os dados vao ser tirados
        # f'{}' = `${}`
        response = fetcher(f'{base_url}?page={page}')
        # lendo o response.text
        selector = Selector(text=response)
        # fazer uma iteracao dentro dos dados coletados(selector)
        # usando o .css acessar a classe .tec--list__item
        # dentro dela o elemento h3 e dentro dele o elemento a
        # do elemento a pegar o atributo href(a::attr(href))
        # getall() pega todos os elementos da pag q tenham as descricoes a cima
        for new in selector.css(".tec--list__item h3 a::attr(href)").getall():
            # repetir o processo do Selector(fetcher)
            # para cada url conseguida no passo anterior
            # assim se tem acesso ao response.text
            # de cada materia da pagina
            new_selector = Selector(text=fetcher(new))
            # adicionar os dados coletados de cada materia na lista news
            news.append({
                # url conseguida a cada volta da iteracao da linha 56
                "url": new,
                # usando o .ccs acessa a classe e dentro dela o texto
                # ( nome_da_classe:: text)
                # get() pra pegar o que foi selecionado
                "title": new_selector.css(".tec--article__header__title::text")
                .get(),
                "timestamp": new_selector.css
                (".tec--timestamp__item time::attr(datetime)")
                .get(),
                "writer": new_selector.css(".tec--author__info__link::text")
                .get(),
                # mesmo processo dos outros, mas o int() passa pra inteiro e o
                # re_first() pega o primeiro matching element
                # alternativa pro get()
                "shares_count":
                int(new_selector.css(
                    ".tec--toolbar__item::text").re_first(r"[0-9]+")),
                "comments_count": int(new_selector.css(
                    "#js-comments-btn::text").re_first(r"[0-9]+")),
                "summary": new_selector.css(".tec--article__body *::text")
                .get(),
                "sources": new_selector.css(".z--mb-16 a::text").getall(),
                "categories": new_selector.css("#js-categories a::text")
                .getall()
            })
        # para n cair em um loop infinito
        page += 1
    return news
