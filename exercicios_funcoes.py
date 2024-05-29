#LOGICA DE PROGRAMAÇÃO EXERCICIOS FUNÇÕES SIMPLES E COMPOSTAS
#DATA: 28/05/2024

#FUNÇÕES SIMPLES

"""
1 - Faça um programa que tenha uma função chamada area(), que receba as dimensões de
um terreno retangular ( largura e comprimento ) e mostre a área do terreno
"""

# def area (largura,comprimento):
#     calc_area = largura * comprimento
#     return calc_area

# print(f"A area do terreno retangular: {area(120,12)}")

"""
2 - Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
"""

# def escreva(texto):
#     texto = texto
#     return texto

# print(escreva("Ola,Mundo!"))
# print(escreva("Opa"))
# print(escreva("Ola, meu nome e Judah!"))

"""
3 - Faça um programa que tenha uma função chamada contador() que receba três
parâmetros: inicio, fim e passo e realize a contagem. Seu programa tem que realizar três
contagens através da função criada
    ● de 1 até 10 de 1 em 1
    ● de 10 até 0 de 2 em 2
    ● uma contagem personalizada   
"""
# from time import sleep

# def contador (i, f, p):
#     if p < 0:
#         p *= -1
#     if p == 0:
#         p = 1
#     print("-=" * 20)
#     print(f"Contagem de {i} ate {f} de {p} em {p}")
#     sleep(2)
    
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f"{cont} ", end='',flush=True)
#             sleep(0.5)
#             cont += p
#         print("FIM!")
#     else:
#         cont = i
#         while cont >= f:
#             print(f"{cont} ", end='',flush=True)
#             sleep(0.5)
#             cont -= p
#         print("FIM!")

# contador (1, 10, 1)
# contador (10, 0, 2)
# print("-=" * 20)
# print("Agora e sua vez de personalizar a contagem!")
# ini = int(input("Inicio: "))
# fim = int(input("Fim: "))
# pas = int(input("Passo: "))
# contador(ini, fim, pas)

"""
4 - Faça um programa que tenha uma função chamada maior() que receba vários
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer
qual deles é maior. 
"""

# from time import sleep

# def maior(*num):
#     cont = maior = 0
#     print("-=" * 30)
#     print("Analisando os valores passados...")
#     for valor in num:
#         print(f"{valor} ", end="",flush=True)
#         sleep(0.3)
#         if cont == 0:
#             maior = valor
#         else:
#             if valor > maior:
#                 maior = valor
#         cont += 1
#     print(f"\nForam informados {cont} valores ao todo.")
#     print(f"O maior valor informado foi {maior}")

# #programa principal
# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(12, 2)
# maior(9)
# maior()

"""
5 - Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da
lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela
função anterior. 
"""

# from random import randint
# from time import sleep

# def sorteia(lista):
#     print('Sorteando 5 valores da lista: ', end='')
#     for cont in range(0,5):
#         n = randint(1,10) 
#         lista.append(n)
#         print(f'{n} ', end='', flush=True)
#         sleep(0.3) 
#     print('PRONTO!')
               
# def somaPar(lista):
#     soma = 0
#     for valor in lista:
#         if valor % 2 == 0:
#             soma += valor
#     print(f'Somando os valores pares de {lista}, temos {soma}')
    
# numeros = list()
# sorteia(numeros)

# somaPar(numeros)

#FUNÇÕES COMPOSTAS

"""
6 - Calcule o fatorial de um número e mostre na tela o resultado
"""

# def fatorial(num):

   # numero = num
    
    # resultado = 1
    # count = 1
    
    # while count <= numero:
    #     resultado *= count
    #     count += 1

    # print(resultado)
    # return num
# fatorial()
