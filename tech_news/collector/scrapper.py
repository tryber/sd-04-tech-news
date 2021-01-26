import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    try:
        """requisição do tipo GET"""
        response = requests.get(url, timeout=timeout)
        """pedindo que a resposta lance uma exceção se o status não seja ok"""
        response.raise_for_status()
        """Coloca uma pausa de 0.5 segundos a cada requisição"""
        time.sleep(delay)
    except (requests.HTTPError, requests.ReadTimeout):
        """Em caso de erro retorna uma string vazia"""
        return ""
    else:
        """conteudo recebido da requisição"""
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
