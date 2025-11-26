from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    TimeoutException
)
from bs4 import BeautifulSoup
import pandas as pd
import time


# === FUNÇÃO DE CLIQUE SEGURO ===
def safe_click(driver, by, selector, timeout=10, retries=3):
    """
    Tenta clicar em um elemento com segurança.
    Faz tentativas normais e, se necessário, usa JavaScript como fallback.
    """
    for tentativa in range(retries):
        try:
            elemento = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, selector))
            )
            elemento.click()
            return True

        except (ElementClickInterceptedException, ElementNotInteractableException):
            print(f"[Aviso] Tentativa {tentativa+1}: elemento não clicável, tentando novamente...")
            time.sleep(1)

        except StaleElementReferenceException:
            print(f"[Aviso] Tentativa {tentativa+1}: elemento mudou no DOM, recarregando...")
            time.sleep(1)

        except TimeoutException:
            print("[Erro] Elemento não encontrado dentro do tempo limite.")
            break

    # Tenta via JavaScript se falhar tudo
    try:
        elemento = driver.find_element(by, selector)
        driver.execute_script("arguments[0].click();", elemento)
        print("[Info] Clique realizado via JavaScript.")
        return True
    except Exception as e:
        print(f"[Erro] Falha ao clicar mesmo via JavaScript: {e}")
        return False


# === CONFIGURAÇÃO DO NAVEGADOR ===
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# === ACESSA O SITE ===
driver.get("https://quotes.toscrape.com/login")

# === FAZ LOGIN (simulado, site de teste) ===
usuario = wait.until(EC.presence_of_element_located((By.ID, "username")))
senha = driver.find_element(By.ID, "password")

usuario.send_keys("admin")
senha.send_keys("1234")

safe_click(driver, By.CSS_SELECTOR, "input[type='submit']")

# === NAVEGA E EXTRAI DADOS DE VÁRIAS PÁGINAS ===
dados = []

while True:
    # Espera o conteúdo da página carregar
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))

    # Analisa o HTML
    soup = BeautifulSoup(driver.page_source, "lxml")

    # Extrai todas as citações
    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        texto = q.find("span", class_="text").text.strip()
        autor = q.find("small", class_="author").text.strip()
        tags = [t.text for t in q.find_all("a", class_="tag")]
        dados.append({
            "texto": texto,
            "autor": autor,
            "tags": ", ".join(tags)
        })

    # Verifica se há um botão "Next"
    next_btn = soup.find("li", class_="next")
    if next_btn:
        link_prox = "https://quotes.toscrape.com" + next_btn.a["href"]
        driver.get(link_prox)
    else:
        break

# === SALVA OS DADOS EM CSV ===
df = pd.DataFrame(dados)
df.to_csv("citacoes.csv", index=False, encoding="utf-8-sig")

print(f"✅ Extraídas {len(dados)} citações e salvas em 'citacoes.csv'.")

driver.quit()