# modulo par fazer requisicoes
# (https://www.w3schools.com/python/module_requests.asp)
import requests
# modulo time que tem varias funcoes para lidar com tempo,
# sleep funciona como setTimeOut
# (https://www.programiz.com/python-programming/time/sleep)
from time import sleep


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
        print(response)
        # retornos do resquests
        # (https://www.w3schools.com/python/ref_requests_response.asp)
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
