import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parents[1] / "data" / "vendas.db"

with sqlite3.connect(db_path) as conn:
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cur.fetchall())
