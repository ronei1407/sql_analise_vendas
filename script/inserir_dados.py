import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parents[1] / "data" / "vendas.db"

clientes = [
    (1, "Ana", "Rio de Janeiro", "RJ"),
    (2, "Carlos", "São Paulo", "SP"),
    (3, "Marcos", "Curitiba", "PR"),
    (4, "Paula", "Recife", "PE"),
]

produtos = [
    (1, "Notebook", "Eletrônicos", 3500.0),
    (2, "Mouse", "Eletrônicos", 80.0),
    (3, "Teclado", "Eletrônicos", 150.0),
    (4, "Monitor", "Eletrônicos", 1200.0),
    (5, "Cadeira", "Escritório", 900.0),
]

pedidos = [
    (1, 1, "2024-01-05"),
    (2, 2, "2024-01-10"),
    (3, 3, "2024-02-02"),
    (4, 1, "2024-02-15"),
    (5, 4, "2024-03-01"),
]

itens = [
    (1, 1, 1, 2),  # pedido 1, notebook, 2
    (2, 2, 2, 5),  # pedido 2, mouse, 5
    (3, 3, 3, 3),  # pedido 3, teclado, 3
    (4, 4, 4, 1),  # pedido 4, monitor, 1
    (5, 5, 5, 2),  # pedido 5, cadeira, 2
]

with sqlite3.connect(db_path) as conn:
    conn.execute("PRAGMA foreign_keys = ON;")

    # para poder rodar o script mais de uma vez sem duplicar tudo
    conn.execute("DELETE FROM itens_pedido;")
    conn.execute("DELETE FROM pedidos;")
    conn.execute("DELETE FROM produtos;")
    conn.execute("DELETE FROM clientes;")

    conn.executemany("INSERT INTO clientes VALUES (?, ?, ?, ?);", clientes)
    conn.executemany("INSERT INTO produtos VALUES (?, ?, ?, ?);", produtos)
    conn.executemany("INSERT INTO pedidos VALUES (?, ?, ?);", pedidos)
    conn.executemany("INSERT INTO itens_pedido VALUES (?, ?, ?, ?);", itens)

print("✅ Dados inseridos com sucesso!")
