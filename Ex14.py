#LÓGICA E ALGORITMO DE PROGRAMAÇÃO
#JUDAH BENJAMIN
#DATA: 20/03/2024
#EXERCICIOS FOR

#EXERCÍCIO #01

"""
Ler dois numeros, somar esses dois numeros lidos e imprimir 3 vezes na tela.       
"""

"""
    for x in range(3):
        numero_1 = int(input("Digite o 1° numero: "))
        numero_2 = int(input("Digite o 2° numero: "))
    
        soma = numero_1 + numero_2
        print("A soma e {}".format(soma))
"""
    
    
#EXERCICIO #02

"""
Par ou ímpar:
O usuário digita um número.
O programa verifica se o número é par ou ímpar e exibe a mensagem "O número é par" ou "O número é ímpar".    
"""

"""
num = 0

while num < 10:
    for x in range(10):
        if num % 2 == 0:
            print(f"O numero {x} e PAR!")
        else:
            print(f"O numero {x} e IMPAR!")
        num += 1 
"""

"""
    for x in range(10):
    numero = int(input("Digite um numero: "))
    
    if numero % 2 == 0:
        print("O numero e PAR!")
    else:
        print("O numero e IMPAR!")
"""
        
#EXERCICIO #03

"""
Maior, menor ou igual:

O usuário digita dois números.
O programa verifica se o primeiro número é maior, menor ou igual ao segundo número e exibe a mensagem "O primeiro número é maior", "O primeiro número é menor", ou "Os números são iguais".   
"""

"""
for x in range(5):
    print("=======================================")
    num_1 = int(input("Digite o primeiro numero: "))
    num_2 = int(input("Digite o segundo numero: "))
    
    if num_1 > num_2:
        print("O primeiro numero e maior")
    elif num_1 < num_2:
        print("O primeiro numero e menor")
    else:
        print("Os numeros sao iguais")
    print("=======================================")
"""


#EXERCICIO #04
    
"""
Positivo ou negativo:

O usuário digita um número.
O programa verifica se o número é positivo ou negativo e exibe a mensagem "O número é positivo" ou "O número é negativo".
"""
    
"""
for c in range(4):
    print("=======================================")
    num = int(input("Digite um numero: "))
         
    if num > 0:
         print("O numero e POSITIVO!")
    else:
        print("O numero e NEGATIVO!")
    print("=======================================")     
"""
    
#EXERCICIO #05

"""
Calculadora de IMC:

O usuário digita seu peso e altura.
O programa calcula o IMC do usuário e exibe a mensagem "Abaixo do peso", "Peso normal", "Sobrepeso", ou "Obesidade".   
"""

"""
    for c in range(3):
    print("============== CALCULO IMC =============")
    usuario = input("Digite o nome: ")
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    
    calculo_imc = peso / altura**2
    print(f"Peso: {calculo_imc:.2f}")
    
    if calculo_imc < 18.5:
        print("Abaixo do peso!")
    elif calculo_imc >= 18.5 and calculo_imc <= 24.9:
        print("Peso Normal")
    elif calculo_imc >= 25 and calculo_imc <= 29.9:
        print("Sobrepeso")
    elif calculo_imc >= 30 and calculo_imc <= 39.9:
        print("Obesidade")
    elif calculo_imc >= 40:
        print("Muito Obeso")
    print("=======================================")   
"""

#EXERCICIO #06

"""
    Simulador de restaurante:

    O usuário pode escolher pratos e bebidas do menu.
    O programa calcula o valor total da conta.   
"""

"""
class Pratos():
    def __init__(preco, prato1, prato2, prato3, prato4) -> None:
        pass
        preco.prato1 = 30.90
        preco.prato2 = 25.00
        preco.prato3 = 10.00
        preco.prato4 = 37.80
"""
        
    