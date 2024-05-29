#LOGICA DE PROGRAMAÇÃO EXERCICIOS FUNÇÕES SIMPLES E COMPOSTAS
#DATA: 29/05/2024

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

# def fatorial(numero):
    
#     if numero == 1:
#         return 1
#     else:
#         return numero * fatorial(numero - 1)
    
# print(fatorial(5))
# print(fatorial(15))

"""
7 - Verifica se o número é par ou ímpar 
"""

# from time import sleep

# print("--" * 30)
# print("                   <   PAR OU IMPAR?  >           ")
# print("--" * 30)
# print("-=" * 30)

# def VerificarParImpar (numero):
#     sleep(0.4)
#     if numero % 2 == 0:
#         print(f'O numero {numero} e PAR',flush=True)
#     else: 
#         print(f'O numero {numero} e IMPAR',flush=True)
#     return numero

# VerificarParImpar(2)
# VerificarParImpar(3)
# VerificarParImpar(21780)
# VerificarParImpar(37)
# VerificarParImpar(18)
# VerificarParImpar(10)
# VerificarParImpar(205)
# VerificarParImpar(146)

"""
8 - Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se
uma pessoa tem voto negado, opcional ou obrigatório nas eleições 
"""

# from time import sleep

# print("--" * 30)
# print("                <<<   VOTO ELEITORAL  >>>           ")
# print("--" * 30)
# print("-=" * 30)

# def voto(AnoNascimento):
#     AnoAtual = 2024
#     Idade = AnoAtual - AnoNascimento
#     sleep(0.4)

#     if Idade >= 18 and Idade < 70:
#         print(f'Sua idade e {Idade} <Voto Obrigatorio>', flush=True)
#     elif Idade >= 16 and Idade < 18:
#         print(f'Sua idade e {Idade} <Voto Opcional>', flush=True)
#     elif Idade >= 70:
#         print(f'Sua idade e {Idade} <Voto Opcional>', flush=True)
#     else:
#         print(f'Sua idade e {Idade} <Voto Negado>', flush=True)
        
#     return Idade

# voto(2000)
# voto(2007)
# voto(2009)
# voto(1940)
# voto(2005)
# voto(2001)
# voto(1995)

"""
9 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o
primeiro que indique o número a calcular e o outro chamado show que será um valor lógico
(opcional) indicando se será mostrado ou não na tela o processo de calculo do fatorial 
"""

# from time import sleep
# import math

# def fatorial(num,show=False):
#     calculo = math.factorial(num)
#     print("--" * 30)
#     sleep(0.4)
#     print(f'Valor digitado: {num}',flush=True)
#     sleep(0.4)
#     show = input('Deseja mostrar o calculo? [S/N] ')
    
#     if show in "Ss":
#         sleep(0.4)
#         print(f'O fatorial de {num} e {calculo}',flush=True)
#         return show
#     else:
#         sleep(0.4)
#         print('CALCULO ENCERRADO...')
        
# fatorial(10,'')
# fatorial(5,'')
# fatorial(11,'')
# fatorial(17,'')
# fatorial(45,'')

"""
10 - Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz
de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
corretamente
"""

# def ficha(jog='<desconhecido>',gol=0):
#     print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# n = input('Nome do Jogador: ')
# g = input('Numero de Gols: ')
# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0
# if n.strip() == '':
#     ficha(gol = g)
# else:
#     ficha(n, g)

"""
11 - Crie um programa que tenha a função leiaInt() que vai funcionar de forma semelhante à
função input() do python, só que fazendo a validação para aceitar apenas um valor
numérico. Ex n = leiaInt(’Digite um n’) 
"""

# from time import sleep

# def leiaInt():
#     sleep(0.5)
#     leiaInt = input
#     n = leiaInt('Digite um numero: ')

#     if n.isnumeric():
#         sleep(0.5)
#         n = int(n)
#         print(f'O numero digitado foi {n}',flush=True)
#     else:
#         print('O valor NAO e numerico.')
#     print("-=" * 30)
#     print('<FIM...>')
# leiaInt()

"""
12 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornando um dicionário com as seguinte informações:
● Quantidade de notas
● a maior nota
● a menor nota
● a média da turma
● a situação ( opcional )       
"""

# def notas(*n, sit=False):
#     """
#     --> Funcao para analisar notas e situacoes de varios alunos
#     :param n: uma ou mais notas dos alunos (aceita varias)
#     :param sit: valor opcional, indicando se deve ou nao adicionar a situacao.
#     :return: dicionario com varias informações sobre a situacao da turma.
#     """
#     r = dict()
#     r['total'] = len(n)
#     r['maior'] = max(n)
#     r['menor'] = min(n)
#     r['media'] = sum(n)/len(n)
#     if sit:
#         if r['media'] >= 7:
#             r['situacao'] = 'BOA'
#         elif r['media'] >= 5:
#             r['situacao'] = 'RAZOAVEL'
#         else:
#             r['situacao'] = 'RUIM'    
#     return r

# resp = notas(5.5, 2.5, sit=True)
# print(resp)
# # help(notas)

"""
13 -  Faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o
comando e o manual vai aparecer. Quando o usuário digitar a palavra “fim” o programa será
encerrado, também utilize cores  
"""

# from time import sleep
# c = ('\033[m',        #0 - sem cores
#      '\033[0;30;41m', #1 - vermelho   
#      '\033[0;30;42m', #2 - verde
#      '\033[0;30;43m', #3 - amarelo
#      '\033[0;30;44m', #4 - azul
#      '\033[0;30;45m', #5 - roxo
#      '\033[7;30m'     #6 - branco
#      );

# def ajuda(com):
#     titulo(f'Acessando o manual do comando \'{com}\'', 4)
#     print(c[6], end='')
#     help(com)
#     print(c[0], end='')
#     sleep(2)
    
# def titulo(msg, cor = 0):
#     tam = len(msg) + 4
#     print(c[cor], end='')
#     print('~' * tam)
#     print(f' {msg}')
#     print('~' * tam)
#     print(c[0], end='')
#     sleep(1)

# comando = ''
# while True:
#     titulo('SISTEMA DE AJUDA PyHELP', 2)
#     comando = input("Funcao ou biblioteca > ")
#     if comando.upper() == 'FIM':
#         break
#     else:
#         ajuda(comando)
# titulo('ATE LOGO', 1)

