#10. Agregação de Dados por Categoria
#Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
#vendas = [{"categoria": "eletrônicos", "valor": 1200},{"categoria": "livros", "valor": 200},{"categoria": "eletrônicos", "valor": 800}

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda['categoria']
    valor = venda['valor']
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor
print(total_por_categoria)