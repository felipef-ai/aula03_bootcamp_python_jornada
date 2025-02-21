### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = 40
preço = 20

if quantidade > 0:
    print("Dados Válidos")
else:
    print("Dados Inválidos")
if preço > 0:
    print("Dados Válidos")
else:
    print("Dados Inválidos")