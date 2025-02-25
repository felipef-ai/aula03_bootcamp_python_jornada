#Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

# Inicializa as variáveis para o controle do loop
nome_valido = False
salario_valido = False
bonus_valido = False

# Loop para verificar o nome
while not nome_valido:
    try:
        nome = input("Digite seu nome: ")
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Loop para verificar o salário
while not salario_valido:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

# Loop para verificar o bônus
while not bonus_valido:
    try:
        bonus = float(input("Digite o valor do bônus recebido: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

bonus_recebido = 1000 + salario * bonus  # Exemplo simples de cálculo de bônus

# Imprime as informações para o usuário
print("-="*50)
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")