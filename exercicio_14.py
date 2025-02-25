#14. Tentativas de Conexão
#Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

tentativas_maximas = 4
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    if True:
        print("CONEXÃO BEM SUCEDIDA!")
        break
    tentativa +=1
else:
    print("FALHA AO CONECTAR APÓS VÁRIAS TENTATIVAS")