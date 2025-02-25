#15. Processamento de Dados com Condição de Parada
#Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, 4, 5]

i = 0
while i < len(itens):
    if itens[i] == 5:
        print("Parada encontrada, encerrando o processamento.")
        break
    # Processa o item

    print("=-"*33)
    print(f"Processando item: {itens[i]}")
    i += 1