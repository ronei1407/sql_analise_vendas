import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parents[1] / "data" / "vendas.db"
sql_path = Path(__file__).resolve().parent / "queries.sql"

content = sql_path.read_text(encoding="utf-8")

# remove comentários e linhas vazias
lines = []
for line in content.splitlines():
    s = line.strip()
    if not s or s.startswith("--"):
        continue
    lines.append(line)

queries = [q.strip() for q in "\n".join(lines).split(";") if q.strip()]

with sqlite3.connect(db_path) as conn:
    for i, q in enumerate(queries, start=1):
        print(f"\n=== Query {i} ===")
        cur = conn.execute(q)
        rows = cur.fetchall()
        for r in rows:
            print(r)
