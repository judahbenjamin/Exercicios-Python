#EXERCICIO OPERADORES ARITMETICOS
# JUDAH BENJAMIN
# DATA: 29/02/2024

"""
1 - Criar uma calculadora simples em Python que utilize os operadores aritméticos para realizar operações básicas: soma, subtração, multiplicação e divisão.
Instruções:
Crie um script Python que solicite ao usuário dois números e um operador.
Utilize os operadores aritméticos +, -, *, / para realizar a operação desejada.
Imprima o resultado da operação, informando os números e o operador utilizado.
"""

n1 = int(input("Informe o primeiro numero:"))
n2 = int(input("Informe o segundo numero:"))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
resto = n1 % n2
divisao_inteira = n1 // n2

print("A soma do primeiro numero e o segundo numero e:", soma)
print("A subtracao do primeiro numero e o segundo numero e:", subtracao)
print("A multiplicacao do primeiro numero e o segundo numero e:", multiplicacao)
print("A divisao do primeiro numero e o segundo numero e:", divisao)
print("O resto do primeiro numero e o segundo numero e:", resto)
print("A divisao  inteira do primeiro numero e o segundo numero e:", divisao_inteira)