import sqlite3
from pathlib import Path

# caminho do banco
base_dir = Path(__file__).resolve().parents[1]
db_path = base_dir / "data" / "vendas.db"
db_path.parent.mkdir(exist_ok=True)

sql = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome TEXT,
    cidade TEXT,
    estado TEXT
);

CREATE TABLE IF NOT EXISTS produtos (
    id_produto INTEGER PRIMARY KEY,
    nome TEXT,
    categoria TEXT,
    preco REAL
);

CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    data_pedido TEXT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE IF NOT EXISTS itens_pedido (
    id_item INTEGER PRIMARY KEY,
    id_pedido INTEGER,
    id_produto INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);
"""

with sqlite3.connect(db_path) as conn:
    conn.executescript(sql)

print("✅ Banco e tabelas criados em:", db_path)
