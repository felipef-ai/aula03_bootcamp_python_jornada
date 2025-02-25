### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = range (1,11)
pares = [v for v in numeros if v % 2 == 0]
print(f'Os números pares são: {pares}')