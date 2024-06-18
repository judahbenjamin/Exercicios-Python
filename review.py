#ALGORITMO E LÓGICA DE PROGRAMAÇÃO - REVISÃO
#DATA: 18/06/2024
#JUDAH BENJAMIN

"""
1. Declaração de Variáveis:

Crie um programa que declare variáveis para armazenar os seguintes dados:

Nome completo
Idade
Altura (em metros)
Peso (em kg)
Imprima os valores das variáveis na tela.        
"""

# Nome_completo = input('Digite seu nome completo: ')
# Idade = int(input('Digite sua idade: '))
# Altura = float(input('Digite sua altura (em metros): '))
# Peso = float(input('Digite seu peso (em kg): '))
# print("-="*30)
# print(f'Nome completo: {Nome_completo}\nIdade: {Idade}\nAltura: {Altura}m\nPeso: {Peso}')

"""
2. Expressões Aritméticas:

Crie um programa que calcule a soma, diferença, produto e quociente de dois números quaisquer. Utilize 
variáveis para armazenar os números e as operações.      
"""

# N1 = int(input('Digite o 1° numero: '))
# N2 = int(input('Digite o 2° numero: '))
# print()
# print('-='*30)

# soma = N1 + N2
# diferenca = N1 - N2
# produto = N1 * N2
# quociente = N1 / N2

# print(f'A soma de {N1} e {N2}: {soma}')
# print(f'A diferenca de {N1} e {N2}: {diferenca}')
# print(f'O produto de {N1} e {N2}: {produto}')
# print(f'O quociente de {N1} e {N2}: {quociente}')

"""
3. Expressões Lógicas:

Crie um programa que verifique se um número inteiro é par ou ímpar. 
Utilize o operador % para realizar a verificação.     
"""

# Num = int(input('Digite um numero inteiro: '))

# if Num % 2 == 0:
#     print(f'O numero {Num} e PAR.')
# else:
#     print(f'O numero {Num} e IMPAR.')

"""
4. Expressões Relacionais:

Crie um programa que compare dois números quaisquer e imprima na tela se 
o primeiro número é maior, menor ou igual ao segundo.   
"""

# N1 = int(input('Digite o 1° numero: '))
# N2 = int(input('Digite o 2° numero: '))

# if N1 > N2:
#     print(f'O numero {N1} e MAIOR que {N2}.')
# elif N1 < N2:
#     print(f'O numero {N1} e MENOR que {N2}.')
# elif N1 == N2:
#     print(f'O numero {N1} e IGUAL a {N2}')

"""
5. Estrutura de Controle if:

Crie um programa que peça ao usuário um 
número inteiro e imprima na tela se o número for positivo, negativo ou zero.
"""

# NUM = int(input('Digite um numero inteiro: '))
# print('-='*30)

# if NUM > 0:
#     print(f'O numero {NUM} e POSITIVO.')
# elif NUM < 0:
#     print(f'O numero {NUM} e NEGATIVO.')
# elif NUM == 0:
#     print(f'O numero {NUM} e ZERO')

"""
6. Estrutura de Controle while:

Crie um programa que peça ao usuário um número inteiro positivo e imprima 
na tela os números de 1 até o número digitado, contando de 1 em 1.  
"""

# from time import sleep

# cont = 0

# NUM = int(input('Digite um numero inteiro positivo: '))
# print("=-"*30)
# print()
# while cont < NUM:
#     print(cont,flush=True)
#     sleep(0.4)
#     cont += 1
    
# print(f'\nPROGRAMA FINALIZADO...')

"""
7. Estrutura de Controle for:

Crie um programa que imprima na tela os números pares de 1 a 20, utilizando um loop for.   
"""

# num = 20

# print('OS PARES:')
# print()
# for num in range(num):
#     if num % 2 == 0:
#         print(f'O numero {num} e PAR')

"""
8. Desafio 1:

Crie um programa que calcule a média aritmética de três notas de um aluno. 
Utilize variáveis para armazenar as notas e a média.
"""

# from time import sleep

# ALUNO = input('ALUNO: ')
# Nota_1 = float(input('NOTA 1: '))
# Nota_2 = float(input('NOTA 2: '))
# Nota_3 = float(input('NOTA 3: '))

# media = (Nota_1+Nota_2+Nota_3)/3

# print('=-'*30)
# sleep(0.4)
# print(f'ALUNO: {ALUNO}',flush=True)
# print(f'MEDIA: {media:.2f}',flush=True)