#LÓGICA DE PROGRAMAÇÃO MINI TORNEIO
#DATA: 04/06/2024

"""
1. Ler um 5 números e verificar se ele é par ou ímpar.
Entrada: Leitura de 5 números
Saída: Exemplo( O número 10 é par)
"""

# from time import sleep

# print("=" * 30)
# print("         PAR OU IMPAR   ")
# print("=" * 30)

# par_impar = []
# cont = 1

# while cont < 6:
#     num = int(input(f'Digite o {cont} numero: '))
#     par_impar.append(num)
#     cont += 1
# print("-=" * 30)
# for n in par_impar:
#     sleep(0.5)
#     if n % 2 == 0:
#         print(f'O numero {n} e PAR!',flush=True)
#     else:
#         print(f'O numero {n} e IMPAR!',flush=True)
# print(f'PROGRAMA FINALIZADO...')

"""
2. Ler um vetor de 5 números inteiros e mostre cada número
juntamente com a sua posição na lista.
Entrada: Leitura de 5 números
Saída: Exemplo( Numero 10, posição 2 do vetor)
"""
# from time import sleep

# numeros_int = [2, 10, 34, 67, 22]
# print(f'Os cinco numeros inteiros sao: {numeros_int}')
# print('-='*30)
# for i in numeros_int:
#     sleep(0.5)
#     print(f'Numero {i}, posicao {numeros_int.index(i)} do vetor',flush=True)
# print('PROGRAMA FINALIZADO...')

"""
3. Crie um programa que peça 10 números inteiros e apresente: a
média, o maior e o menor.
Entrada: Leitura de 10 números
Saída: Exemplo( A média = 20, o maior = 9 e o menor= 3)    
"""

# n = []
# cont = 0

# while cont < 10:
#     numero = int(input('Digite um numero: '))
#     n.append(numero)
#     cont += 1
# print('-='*30)

# media = sum(n)/len(n)

# print(f'A media = {media}, o maior = {max(n)} e o menor = {min(n)}')

"""
4. Faça um algoritmo que leia um conjunto de números (X) e imprima sua 
soma (Soma) e sua média (Media). Admita que o valor 50 é utilizado 
como sentinela para fim de leitura.  
Entrada: Leitura de 1 a 50 números  
Saída: Exemplo(Soma=6 Media=2)  
"""

# n = []
# cont = 0
# quant = int(input('Digite a quantidade de numeros: '))
    
# while cont < quant:
#     num = int(input('Digite o numero: '))
#     if num == 50:
#         print('PROGRAMA ENCERRADO...')
#         media = False
#         break
#     else:
#         n.append(num)
#         cont += 1
#         media = sum(n)/len(n)

# print(f'Soma = {sum(n)}, Media = {media}')
