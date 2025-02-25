#12. Validação de Entrada
#Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

numero = int(input("Digite um número entre 1 e 5: "))
while numero <1 or numero >5:
    print("Número fora do intervalo solicitado")
    numero = int(input("Digite um número entre 1 e 5"))
print('-='*33)
print("Número válido!")