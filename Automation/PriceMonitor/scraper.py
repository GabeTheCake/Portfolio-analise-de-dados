import requests
from bs4 import BeautifulSoup


def coletar_preco(url: str):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    produto = soup.select_one("div.thumbnail")
    if not produto:
        raise ValueError("Nenhum produto encontrado")

    nome = produto.select_one("a.title")
    preco = produto.select_one("h4.price")

    if not nome or not preco:
        raise ValueError("Estrutura do site mudou")

    nome = nome.get_text(strip=True)
    preco_texto = preco.get_text(strip=True)

    preco = float(preco_texto.replace("$", "").replace(",", ""))

    return nome, preco
