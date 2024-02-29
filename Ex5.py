#EXERCICIO OPERADORES RELACIONAIS
# JUDAH BENJAMIN
# DATA: 29/02/2024

""" 1 - Criar um algoritmo em Python que utiliza operadores relacionais para comparar valores e tomar decisões.
Instruções:
Crie um script Python que solicite ao usuário dois números inteiros.
Utilize os operadores relacionais ==, !=, <, >, <=, >= para comparar os números digitados.
Imprima mensagens informando o resultado da comparação, utilizando linguagem clara e concisa."""


Num1 = int(input("Digite o primeiro numero:"))
Num2 = int(input("Digite o segundo numero:"))

igual = Num1 == Num2
diferente = Num1 != Num2
menor = Num1 < Num2
maior = Num1 > Num2
menor_igual = Num1 <= Num2
maior_igual = Num1 >= Num2

print("Numero 1 e igual a Numero 2?",igual)
print("Numero 1 e diferente de Numero 2?",diferente)
print("Numero 1 e menor que Numero 2?",menor)
print("Numero 1 e maior que  Numero 2?",maior)
print("Numero 1 e menor ou igual a Numero 2?",menor_igual)
print("Numero 1 e maior ou igual a Numero 2?",maior_igual)