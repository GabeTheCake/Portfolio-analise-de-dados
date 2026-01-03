import smtplib
from email.message import EmailMessage
from config import EMAIL_REMETENTE, EMAIL_SENHA, EMAIL_DESTINO

def enviar_alerta(produto: str, preco_antigo: float, preco_novo: float):
    msg = EmailMessage()
    msg["Subject"] = f"Alerta de preço: {produto}"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = EMAIL_DESTINO

    msg.set_content(
        f"""
O preço do produto mudou!

Produto: {produto}
Preço anterior: R$ {preco_antigo:.2f}
Novo preço: R$ {preco_novo:.2f}
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_REMETENTE, EMAIL_SENHA)
        smtp.send_message(msg)
