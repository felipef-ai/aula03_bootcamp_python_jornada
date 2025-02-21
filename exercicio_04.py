### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

#idade = 25  # Exemplo de valor, substitua com input do usuário se necessário
#email = "usuario@exemplo.com"  # Exemplo de valor, substitua com input do usuário se necessário


idade = 20    #int(input("Digite sua idade: "))
email = "usuario@exemplo.com"   #input("Digite o seu e-mail: ")
try:
    if not 18 <= idade <= 65:
        print("Idade não permitida")
    elif "@" not in email or "." not in email:
        print("Esse e-mail não é válido!")
    else:
        print("Permitido o acesso!")
except NameError:
        print("E-mail inválido")
