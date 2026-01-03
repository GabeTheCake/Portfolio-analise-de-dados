from config import URL_PRODUTO, LIMIAR_VARIACAO
from scraper import coletar_preco
from database import inicializar_db, salvar_preco, obter_ultimo_preco
from notifier import enviar_alerta

def main():
    inicializar_db()

    produto, preco_atual = coletar_preco(URL_PRODUTO)
    preco_anterior = obter_ultimo_preco(produto)

    if preco_anterior:
        variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100

        if abs(variacao) >= LIMIAR_VARIACAO:
            enviar_alerta(produto, preco_anterior, preco_atual)

    salvar_preco(produto, preco_atual)
    print(f"[OK] {produto} - R$ {preco_atual:.2f}")

if __name__ == "__main__":
    main()
