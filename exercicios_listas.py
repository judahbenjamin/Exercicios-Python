#LOGICA DE PROGRAMAÇÃO EXERCICIOS LISTAS SIMPLES E COMPOSTAS
#DATA: 22/05/2024

"""
1 - Faça um programa que leia 5 valores numéricos e guarde-os em uma
 lista. No final, mostre qual foi o maior e o menor valor digitado e as suas
 respectivas posições na lista
"""

# valores_numericos = []
# cont = 0

# while cont < 5:
#     num = int(input("Digite um numero: "))
#     valores_numericos.append(num)
#     cont += 1
# print(f"Lista dos valores numericos: {valores_numericos}")

# maior = max(valores_numericos)
# menor = min(valores_numericos)

# print(f"O maior valor digitado da lista e {maior} e o menor e {menor}.")

# if maior in valores_numericos and menor in valores_numericos:
#     print(f"O numero {maior} esta na posicao {valores_numericos.index(maior)+1} da lista!")
#     print(f"O numero {menor} esta na posicao {valores_numericos.index(menor)+1} da lista!")

"""
2 - Crie um programa onde o usuário possa digitar vários valores
 numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
 ele não será adicionado. No final, serão exibidos todos os valores únicos
 digitados, em ordem crescente.
"""

# lista_valores=[]

# x = 0
# while x < 10:
#     valor = float(input("Digite um valor numérico: "))
#     if valor not in lista_valores:
#         lista_valores.append(valor)
#         print(f"Valor {valor} adicionado com sucesso!")
#     else:
#         print(f"Valor {valor} já existe na lista. Ignorado.")
#     x += 1
# print(lista_valores)

"""
3 - Crie um programa onde o usuário possa digitar cinco valores numéricos
 e cadastre-os em uma lista, já na opção correta de inserção ( sem usar o
 sort() ). No final, mostre a lista ordenada na tela.
"""

# valores = []
# i = 0

# while i < 5:
#     valor = int(input("Digite um valor numerico: "))
#     valores.append(valor)
#     i += 1
# print(f"A lista ja ordenada: {valores}")
# # valores.sort()
# # print(f"A lista ja ordenada: {valores}")

"""
4 - Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, mostre:
    ● Quantos números foram digitados
    ● A lista de valores, ordenada de forma decrescente
    ● Se o valor 5 foi digitado e está ou não na list
"""

# numeros = []

# i = 0

# while i < 10:
#     num = int(input("Digite um valor: "))
#     numeros.append(num)
#     i += 1
# print(f"Lista dos numeros: {numeros}")

# quantidade_num = len(numeros)
# print(f"Quantidade de numeros digitados: {quantidade_num}")
# numeros.sort(reverse=True)
# print(f"A ordem decrescente: {numeros}")

# if 5 in numeros:
#     print(f"O valor 5 foi digitado e esta na posicao {numeros.index(5)+1} da lista")
# else:
#     print("O valor 5 nao foi digitado e nao esta na lista!")

"""
5 - Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores
 pares e os valores ímpares digitados, respectivamente. Ao final mostre o
 conteúdo das três listas geradas.    
"""

# numeros_aleatorios = []
# numeros_par = []
# numeros_impar = []

# cont = 0

# while cont < 10:
#     num = int(input("Digite um valor: "))
#     numeros_aleatorios.append(num)
#     cont += 1

# for x in numeros_aleatorios:
#     if x % 2 == 0:
#         numeros_par.append(x)
#     else:
#         numeros_impar.append(x)
        
# print(f"Os numeros digitados: {numeros_aleatorios}")
# print(f"Os numeros pares {numeros_par}")
# print(f"Os numeros impares: {numeros_impar}")

"""
6 - Crie um programa onde o usuário digite uma expressão qualquer que
 use parênteses. Seu aplicativo deverá analisar se a expressão passada está
 com os parênteses abertos e fechados na ordem correta.   
"""

# print('\33c')
# exp = input('Digite sua expressão: ').split()
# #OBS: Coloque um espaço depois do parenteses inicial e antes do parenteses final
# print(exp[0])
# print(exp[3])

# for x in exp:
#     if x == '(':
#         print("OK")
#     elif x == ')':
#         print("OK 1")
#     else:
#         print("Negado")
# lista = list()
# for simb in exp:
#     if simb == '(':
#         lista.append('(')
#     elif simb == ')':
#         if len(lista) > 0:  
#             lista.pop()
#         else:
#             lista.append(')')
#             break
# if len(lista) == 0:
#     print('Expressão valida !')
# else:
#     print('Expressão invalida..')


