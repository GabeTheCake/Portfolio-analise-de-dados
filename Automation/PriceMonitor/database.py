import sqlite3
from datetime import datetime
from pathlib import Path

# Caminho absoluto e seguro
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "prices.db"


def inicializar_db():
    """Cria pasta e tabela se não existirem"""
    DATA_DIR.mkdir(exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS prices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto TEXT NOT NULL,
                preco REAL NOT NULL,
                data TEXT NOT NULL
            )
        """)


def salvar_preco(produto: str, preco: float):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO prices (produto, preco, data) VALUES (?, ?, ?)",
            (produto, preco, datetime.now().isoformat())
        )


def obter_ultimo_preco(produto: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            """
            SELECT preco FROM prices
            WHERE produto = ?
            ORDER BY id DESC
            LIMIT 1
            """,
            (produto,)
        )
        row = cursor.fetchone()
        return row[0] if row else None
