#13. Consumo de API Simulado
#Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

from time import sleep
pagina_atual = 1
paginas_totais = 5  # Simulação, na prática, isso viria da API
while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais}")
    # Aqui iria o código para processar os dados da página
    pagina_atual += 1

print("Todas as páginas foram processadas.")