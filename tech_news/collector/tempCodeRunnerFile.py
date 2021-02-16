# modulo par fazer requisicoes
# (https://www.w3schools.com/python/module_requests.asp)
import requests
# modulo time que tem varias funcoes para lidar com tempo,
# sleep funciona como setTimeOut
# (https://www.programiz.com/python-programming/time/sleep)
from time import sleep
# modulo para remover informacoes de html
# (https://parsel.readthedocs.io/en/latest/usage.html)
# from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    # bloco try/except = try/catch
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
        print(response.text)
        # retornos do resquests
        # (https://www.w3schools.com/python/ref_requests_response.asp)
        return response.text


fetch_content("https://www.tecmundo.com.br/novidades?page=1")

