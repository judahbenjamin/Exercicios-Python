#LÓGICA DE PROGRAMAÇÃO MINI TORNEIO
#DATA: 03/06/2024

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

cont = 0

while cont < 10:
    numero = int(input('Digite um numero: '))
    cont += 1
print('-='*30)

