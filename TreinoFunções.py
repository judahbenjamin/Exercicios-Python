#EXERCÍCIOS DE FUNÇÕES
#DATA: 15/04/2024
#BY JUDAH BENJAMIN

#1 - Crie uma função que faça a multiplicação de dois valores.

def multiplicacao (a, b):
    resultado = a * b
    return resultado

print(multiplicacao(2,3))

#2 - Crie uma função que realize um calculo de uma area e de um circulo de um raio.

def calculo_area (altura, largura):
    resultado_calculo = f"A area e: {altura * largura}m2."
    return resultado_calculo

print(calculo_area(10,8))
print(calculo_area(10,10))

import math

def circulo_raio (raio1,raio2):
    calculo = "A area do circulo e: {:.2f}".format(math.pi * raio1 * raio2)
    return calculo

print(circulo_raio(5,5))

#3 - Crie uma função que receba uma quantidade indeterminada de nomes.

def chamada (*nomes):
    for nome in nomes:
        print("Oi, "+ nome + "!")
        
chamada("Joao","Pedro","Tiago","Andre")