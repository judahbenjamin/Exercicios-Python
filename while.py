#LÓGICA E ALGORITMO DE PROGRAMAÇÃO
#MÁRCIO CLAY
#ALUNO: JUDAH
#DATA: 19/03/2024
#ESTRUTURA WHILE

#WHILE - verifica a condição antes de executar o código e é usado quando um número de interações é desconhecido.

#Variáveis
#Tipos de dados
# Operadores
#Manipulação de strings
#If, While, For
#Funções e métodos
#Vetores e Matrizes

print("============== WHILE =================")

numero = 1

while numero <= 15:
    print(numero)
    numero += 1
    
#WHILE e IF

print("================== WHILE e IF =======================")

numero = 1

while numero <= 15:
    if numero % 2 == 0:
        print(f"{numero} e par")
    else: 
        print(f"{numero} e impar")
    numero += 1
    
#Exemplo 2

lista_numeros = [1, 2, 3, 4, 5]

numero = 0

while numero < len(lista_numeros):
    print(lista_numeros[numero])
    numero += 1 
    
#Exemplo 3

print("==================== WHILE e FOR ======================")

numero = 1

while numero <= 10:
    for i in range(2, numero): #in range é uma função que retorna sequencia de numeros. Apenas com numeros inteiros.
        if numero % i == 0:
            break
    else:
        print(f"{numero} e primo.")
    numero += 1        