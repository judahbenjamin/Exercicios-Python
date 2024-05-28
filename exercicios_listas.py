#LOGICA DE PROGRAMAÇÃO EXERCICIOS LISTAS SIMPLES E COMPOSTAS
#DATA: 28/05/2024

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


#LISTAS COMPOSTAS


"""
7 - Faça um programa que leia nome e peso de várias pessoas, guardando
tudo em uma lista. No final mostre:
    ● Quantas pessoas foram cadastradas
    ● Uma listagem com as pessoas mais pesadas
    ● Uma contagem com as pessoas mais leves   
"""

# temp = []
# princ = []
# mai = men = 0

# while True:
#     temp.append(input("NOME: "))
#     temp.append(float(input("PESO: ")))
#     if len(princ) == 0:
#         mai = men = temp[1]
#     else:
#         if temp[1] > mai:
#             mai = temp[1]
#         if temp[1] < men:
#             men = temp[1]
#     princ.append(temp[:])
#     temp.clear()
#     resp = input("Quer continuar? [S/N] ")
#     if resp in "Nn":
#         break
# print('-='*30)
# print(f"Os dados foram {princ}")
# print(f"Ao todo foram cadastrados {len(princ)} pessoas.")
# print(f"O maior peso foi de {mai}Kg. Peso de", end="")
# for p in princ:
#     if p[1] == mai:
#         print(f"[{p[0]}]", end="")
# print()
# print(f"O menor peso foi de {men}Kg. Peso de ", end='')
# for p in princ:
#     if p[1] == men:
#         print(f"[{p[0]}]", end="")
# print()

"""
8 - Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores
pares e impares. No final mostre os valores pares e impares em ordem
crescente 
"""

# valores_num = []
# par = []
# impar = []

# cont = 0

# while cont < 7:
#     numero = int(input("Digite um valor:"))
#     valores_num.append(numero)
#     cont += 1

# for n in valores_num:
#     if n % 2 == 0:
#         par.append(n)
#     else:
#         impar.append(n)
        
# print("-="*30)
        
# print(f"Os numeros pares: {par}")
# print(f"Os numeros impares: {impar}")

# par.sort()
# impar.sort()

# print("-="*30)

# valores_num = [par,impar]
# print(f"Os valores numericos informados ja ordenados: {valores_num}")

"""
9 - Crie um programa que crie uma matriz de dimensão 3 x 3 e preencha
com valores lidos pelo teclado. Mostre a matriz na tela com a formatação
correta.     
"""

# matriz = [[0,0,0],[0,0,0],[0,0,0]]
# for l in range(0,3):
#     for c in range(0,3):
#         matriz [l][c] = int(input(f"Digite um valor para [{l},{c}]: "))
# print("-=" * 30)
# for l in range(0,3):
#     for c in range(0,3):
#         print(f"[{matriz[l][c]:^5}]", end='')
#     print()

"""
10 - Aprimore o desafio anterior, mostrando no final:
    ● A soma de todos os valores pares digitados.
    ● A soma dos valores da terceira coluna
    ● O maior valor da segunda coluna   
"""

# matriz = [[0,0,0],[0,0,0],[0,0,0]]
# spar = mai = scol = 0
# for l in range(0,3):
#     for c in range(0,3):
#         matriz [l][c] = int(input(f"Digite um valor para [{l},{c}]: "))
# print("-=" * 30)
# for l in range(0,3):
#     for c in range(0,3):
#         print(f"[{matriz[l][c]:^5}]", end='')
#         if matriz[l][c] % 2 == 0:
#             spar += matriz[l][c]
#     print()
# print("-=" * 30)
# print(f"A soma dos valores pares e {spar}.")
# for l in range(0,3):
#     scol += matriz[l][2]
# print(f"A soma dos valores da terceira coluna e {scol}.")
# for c in range(0,3):
#     if c == 0:
#         mai = matriz[1][c]
#     elif matriz[1][c] > mai:
#         mai = matriz[1][c]
# print(f"O maior valor da segunda linha e {mai}")

"""
11 - Faça um programa que ajude um jogador da mega sena a criar
 palpites. O programa vai perguntar quantos jogos serão gerados e vai
 sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
 lista composta. Lembrando que os números não podem se repetir.     
"""

# from random import randint
# from time import sleep

# lista = list()
# jogos = list()

# print("-" * 30)
# print("      JOGO MEGA SENA     ")
# print("-" * 30)

# quant = int(input("Quantos jogos voce quer sortear? "))
# tot = 1
# print()
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1,60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1
# print("-=" * 3, f" SORTEANDO {quant} JOGOS", "-=" * 3)
# print()
# for i, l in enumerate(jogos):
#     print(f"Jogo {i+1}: {l}")
#     sleep(1)
# print()
# print("-=" * 5, "< BOA SORTE! >", "-=" * 5)

"""
12 -  Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.  
"""

# ficha = list()

# while True:
#     nome = input('Nome: ')
#     nota1 = float(input("Nota 1: "))
#     nota2 = float(input("Nota 2: "))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome, [nota1, nota2], media])
#     resp = input("Quer continuar? [S/N] ")
#     if resp in "Nn":
#         break
# print("-=" * 30)
# print(f"{"No.":<4}{"NOME":<10}{"MEDIA":>8}")
# print("-" * 26)
# for i, a in enumerate(ficha):
#     print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
# while True:
#     print("-" * 35)
#     opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
#     if opc == 999:
#         print("FINALIZANDO...")
#         break
#     if opc <= len(ficha) - 1:
#         print(f"Notas de {ficha[opc][0]} sao {ficha[opc][1]}")
# print("<<<< VOLTE SEMPRE >>>>")
