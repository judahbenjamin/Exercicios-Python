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

"""
5. Escreva um algoritmo para ler o nome e a idade de uma pessoa, e 
exibir quantos dias de vida ela possui. Considere sempre anos 
completos, e que um ano possui 365 dias.  
Entrada: Leitura nome e idade em anos.  
Saída: Exemplo(MARIA, VOCÊ JÁ VIVEU 6935 DIAS)   
"""

# nome = input('Digite o nome: ')
# idade = int(input('Digite a idade: '))

# ano = 365
# dias_de_vida = idade * ano
# print(f'{nome}, voce ja viveu {dias_de_vida} dias'.upper())

"""
6. Leia os quatro valores correspondentes aos eixos x e y de dois 
pontos do plano, p1 (x1, y1) e p2 (x2, y2) e calcule a distância entre 
eles, mostrando duas casas decimais após a vírgula, conforme a 
fórmula : 
Distância = 
Entrada 
O arquivo de entrada contém duas linhas de dados. O primeiro contém dois 
valores duplos:  x1 y1 e o segundo também contém dois valores duplos com 
um dígito após o ponto decimal: x2 y2 . 
Resultado 
Calcule e imprima o valor da distância usando a fórmula fornecida, com 2 
dígitos após o ponto decimal.
"""

# import math

# x1 = int(input('Digite um valor pra X1: '))
# y1 = int(input('Digite um valor pra Y1: '))

# x2 = int(input('Digite um valor pra X2: '))
# y2 = int(input('Digite um valor pra Y2: '))

# p1 = (x1, y1)
# p2 = (x2, y2)

# distancia = ((x2 - x1)**2 + (y2 - y1)**2)
# raiz_quadrada = math.sqrt(distancia)

# print(f'Resultado: {raiz_quadrada:.2f}')

"""
7. Leia 4 valores inteiros A, B, C e D. Então se B for maior que C e D for 
maior que A e se a soma de C e D for maior que a soma de A e B e se 
C e D forem valores positivos e se A for par, escreva a 
mensagem “Valores aceitos” . Caso contrário, escreva a 
mensagem “Valores não aceitos” (Valores não aceitos). 
Entrada 
Quatro números inteiros A, B, C e D. 
Resultado 
Mostre a mensagem correspondente após a validação dos valores.  
"""

# A = int(input('Digite um valor A: '))
# B = int(input('Digite um valor B: '))
# C = int(input('Digite um valor C: '))
# D = int(input('Digite um valor D: '))

# somaAB = A + B
# print(f'Soma de A e B: {somaAB}')
# somaCD = C + D
# print(f'Soma de C e D: {somaCD}')
# positivo = True

# if B > C and D > A and somaCD > somaAB and C > 0 and D > 0 and A % 2 == 0:
#     print(f'Valores aceitos!')
# else:
#     print(f'Valores nao aceitos!')

"""
8. Ler os anos de nascimento de duas pessoas e calcular suas idades. 
Imprimir o nome e a idade de cada uma e indicar qual é a maior 
idade. 
"""

# ANO_ATUAL = 2024
# nome_pessoa1 = input('Digite o nome da primeira pessoa: ')
# nascimento_pessoa1 = int(input('Digite o ano de nascimento da primeira pessoa: '))

# nome_pessoa2 = input('Digite o nome da segunda pessoa: ')
# nascimento_pessoa2 = int(input('Digite o ano de nascimento da segunda pessoa: '))
# print("-="*30)
# idade1 = ANO_ATUAL - nascimento_pessoa1
# idade2 = ANO_ATUAL - nascimento_pessoa2

# print(f'O nome da 1° pessoa e {nome_pessoa1} e sua idade e {idade1}')
# print(f'O nome da 2° pessoa e {nome_pessoa2} e sua idade e {idade2}')
# print("-="*30)
# if idade1 > idade2:
#     idade_maior = idade1
#     idade_menor = idade2
# else:
#     idade_maior = idade2
#     idade_menor = idade1
    
# print(f'A maior idade e de {idade_maior}')

"""
9. Escreva um programa que leia 6 números. Esses números serão 
apenas positivos ou negativos (desconsidere valores 
nulos). Imprima o número total de números positivos. 
Entrada 
Seis números, positivos e/ou negativos. 
Resultado 
Imprima uma mensagem com o número total de números positivos.  
"""

# cont = 0
# nums = []
# positivos = []

# while cont < 6:
#     num = int(input('Digite um numero: '))
#     nums.append(num)
#     cont += 1
 
# for i in nums:
#     if i > 0:
#         positivos.append(i)
# print("=_"*30)   
# print(f'O numero total de numeros positivos e {len(positivos)}')

"""
10. A empresa ABC decidiu dar um aumento salarial aos seus 
funcionários, conforme tabela a seguir: 

Salário                     |             Taxa de reajuste

0 - 400,00                                      15%     
400,01 - 800,00                                 12%
800,01 - 1.200,00                               10%
1.200,01 - 2.000,00                             7% 
Acima de 2.000,00                               4%

Leia o salário do funcionário, calcule e imprima o novo salario com 
reajuste, com mensagens correspondentes, conforme exemplo abaixo. 

Entrada:
A entrada contém apenas um número de ponto flutuante, com 2 dígitos após 
o ponto decimal. 
Resultado:
Imprima 1 mensagem seguida do valor do novo salário.  
Novo Salario: 1500,25   
"""

# salario = float(input('Digite o salario do funcionario: '))

# if salario >= 0 and salario <= 400.00:
#     calc_salario = salario * (15/100)
#     novo_salario = salario + calc_salario
# elif salario >= 400.01 and salario <= 800.00:
#     calc_salario = salario * (12/100)
#     novo_salario = salario + calc_salario
# elif salario >= 800.01 and salario <= 1200.00:
#     calc_salario = salario * (10/100)
#     novo_salario = salario + calc_salario
# elif salario >= 1200.01 and salario <= 2000.00:
#     calc_salario = salario * (7/100)
#     novo_salario = salario + calc_salario
# elif salario > 2000.00:
#     calc_salario = salario * (4/100)
#     novo_salario = salario + calc_salario
# print('-='*30)
# print(f'O salario do funcionario e R${salario} e o reajuste ficou R${novo_salario}')
