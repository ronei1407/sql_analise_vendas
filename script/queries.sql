-- 1) Listar todos os pedidos com nome do cliente e data
SELECT p.id_pedido, c.nome AS cliente, p.data_pedido
FROM pedidos p
JOIN clientes c ON c.id_cliente = p.id_cliente
ORDER BY p.data_pedido;

-- 2) Faturamento total (JOIN + cálculo)
SELECT SUM(ip.quantidade * pr.preco) AS faturamento_total
FROM itens_pedido ip
JOIN produtos pr ON pr.id_produto = ip.id_produto;

-- 3) Faturamento por mês
SELECT substr(p.data_pedido, 1, 7) AS mes,
       SUM(ip.quantidade * pr.preco) AS faturamento
FROM pedidos p
JOIN itens_pedido ip ON ip.id_pedido = p.id_pedido
JOIN produtos pr ON pr.id_produto = ip.id_produto
GROUP BY mes
ORDER BY mes;

-- 4) Top produtos por faturamento
SELECT pr.nome AS produto,
       SUM(ip.quantidade * pr.preco) AS faturamento
FROM itens_pedido ip
JOIN produtos pr ON pr.id_produto = ip.id_produto
GROUP BY pr.nome
ORDER BY faturamento DESC;
