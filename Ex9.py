#LÓGICA DE ALGORITMO E PROGRAMAÇÃO
#PROF: MARCIO CLAY
#JUDAH BENJAMIN
#DATA: 06/03/2024
#EXERCICIOS

#1) 

"""
produto = input("Digite o produto que voce quer comprar:")
preco_produto = float(input("Digite o preco desse produto:"))

print(f"O seu produto escolhido foi {produto} no preco de R${preco_produto}.")

if preco_produto <= 20.00:
    print("Vou comprar")
else:
    print("Não vou comprar")
       
"""

#2) 

produto = "Feijao_preto"
preco = 25.00
bacon = True

if preco <= 20.00:
    if  bacon != True:
        print("Comprar Tudo!")
else:
    print("Nao comprar!")
    
#3)
"""
print("////// INFORMACOES DE UM INDIVIDUO ////////")

nome = input("Digite o nome do individuo:")
idade = int(input("Digite a idade do individuo:"))
peso = float(input("Digite o peso do individuo:"))
tamanho = float(input("Digite o tamanho do individuo:"))
saude = bool(input("O individuo e saudavel?"))

print(f"Nome do individuo: {nome}")
print(f"Idade do individuo: {idade}")
print(f"Peso do individuo: {peso}")
print(f"Tamanho do individuo: {tamanho}")
print(f"Saude do individuo: {saude}") 

print("//// RESULTADOS ////")

if idade >= 18:
    print("O individuo ja e maior de idade")
    if peso < 100:
        print("Não esta acima do peso")
        if saude == True:
            print("O individuo esta saudavel.")
else:
    print("O individuo e menor.")
    print("O individuo esta acima do peso.")
    print("O individuo nao e saudavel.")  
"""

#4)

raio = 5
PI = 3.14
AreaCirc = PI * raio * raio

print(f"A area da circunferencia sera: {AreaCirc}m2")

#5)

print("///// PAR OU IMPAR //////")

number = 8

if number % 2 == 0 :
    print("O numero e PAR")
else:
    print("O numero e IMPAR")
    
#6)

"""
N = int(input("Digite um numero:"))

if N > 0:
    print("POSITIVO")
elif N < 0:
    print("NEGATIVO")
else:
    print("NULO 0")  
"""

#7)

print("////////// TROCA DE VALORES ////////////")

a = 6
b = 2
c = 10
d = 40


aux = a
a = b
b = aux
aux = c
c = d
d = aux

print(f"A:{a}")
print(f"B:{b}")
print(f"C: {c}")
print(f"D:{d}")

"""
8 - Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longa   
"""

distancia = int(input("Digite a distancia percorrida do carro:"))

if distancia <= 200 :
    preco_passagem = distancia * 0.50
    print("Preco da passagem: R${:.2f}.".format(preco_passagem))
else:
    preco_passagem = distancia * 0.45
    print("Preco da passagem: R${:.2f}.".format(preco_passagem))

print("O preco da passagem foi: R${:.2f}.".format(preco_passagem),"de acordo com a sua velocidade percorrida")

#OBS: A notação :.2f na variável limita a quantidade de casas decimais após o ponto flutuante para 2.

#Ou

"""
distancia = int(input("Digite a distancia percorrida do carro:"))

if distancia <= 200 :
    preco_passagem = distancia * 0.50
    print(f"Preco da passagem: {preco_passagem}")
else:
    preco_passagem = distancia * 0.45
    print(f"Preco da passagem: {preco_passagem}")

print(f"O preco da passagem foi: {preco_passagem} de acordo com a sua velocidade percorroda")
  
"""