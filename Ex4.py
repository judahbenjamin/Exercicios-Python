#LISTA DE EXERCÍCIOS 4
# JUDAH BENJAMIN
# DATA: 28/02/24

"""
1 -Calcular a média de uma lista de números: Crie um programa que receba uma lista de 
números e retorne a média dos valores presentes na lista.
"""

listN = [50, 10, 3, 12, 17, 18, 5, 79]
soma = sum(listN)
media = soma/ len(listN)
print("A media dos numeros e:",media)

#Exemplo2 - Media de notas de alunos

Notas = [2.5, 3.5, 7.0, 8.0]
soma = sum(Notas)
media = soma/ len(Notas)
print("A media das notas e:", media)

"""
2 - Verificar se um número é par ou ímpar: Desenvolva um programa que receba 
um número como entrada e determine se ele é par ou ímpar.
"""

numero = float(input("Digite um numero para saber se ele e par ou impar:"))
resto = numero % 2

if resto == 0 :
    print("Numero Par")
else :
    print("Numero Impar")
    
#if num % 2 == 0: print('Esse número é par! ') else: print('Ele é ímpar!