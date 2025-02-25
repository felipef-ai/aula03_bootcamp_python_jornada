#11. Leitura de Dados até Flag
#Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

dados = []  # Lista para armazenar os valores
while True:  # Loop infinito, interrompido manualmente com 'break'
    entrada = input("Digite um valor (ou 'sair' para terminar): ")
    
    if entrada.lower() == "sair":  # Se o usuário digitar 'sair', sai do loop
        break

    dados.append(entrada)  # Adiciona o valor à lista
print('-='*30)
print("Valores digitados:", dados)  # Mostra os valores coletados