#LÓGICA DE PROGRAMAÇÃO E ALGORITMO
#PROFESSOR: MÁRCIO CLAY
#ALUNO: JUDAH BENJMAIN
#DATA: 29/04/2024

"""
1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.   
"""

# vetor_numeros = [1,2,3,4,5]
# print(f"Os numeros sao: {vetor_numeros}")

"""
2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

# numeros_reais = [1.0,2.4,3.2,4.5,5.0,6.0,7.8,8.9,9.0,10.3]
# numeros_reais.sort(reverse= True)
# print(f"A inversao e: {numeros_reais}")

"""
3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

# notas = [6.0, 7.5, 9.7, 10.0]
# print(f"As notas sao: {notas}")

# soma = sum(notas)
# media = soma/len(notas)
# print(f"A media das notas e: {media}")

"""
4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

# caracteres = ["a","b","c","d","e","p","g","i","j","m"]
# vogal = ["a","e","i","o","u"]
# consoantes = []

# def identificarConsoantes(caracter : str):
#     if caracter not in vogal:
#         consoantes.append(caracter)

# for caracter in caracteres:
#     identificarConsoantes(caracter)
    
# ContarConsoantes = len(consoantes)
# print("Os caracteres sao: {}".format(caracteres))
# print("A quantidade de consoantes encontradas sao: {}".format(ContarConsoantes))
# print("As consoantes sao: {}".format(consoantes))


"""
5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os 
números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
    
"""

# numeros_inteiros = []
# par = []
# impar = []

# for c in range(20):
#     numero = int(input("Digite um numero inteiro:"))
#     numeros_inteiros.append(numero)
    
# def identificarPareImpar (numero : int):
#     if numero % 2 == 0:
#         par.append(numero)
#     else:
#         impar.append(numero)
        
# for numero in numeros_inteiros:
#     identificarPareImpar(numero)

# print(f"A lista dos numeros inteiros:{numeros_inteiros}")
# print(f"Os numeros pares: {par}")
# print(f"OS numeros impares: {impar}")

"""
6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e 
armazene num vetor a média de cada aluno, imprima o número de 
alunos com média maior ou igual a 7.0
""" 

# alunos = 10 #Declaração da quantidade de alunos
# notas = 4 #Declaração da qauntidade de notas

# medias = [] #array vazio para armazenar as medias
# media_sete = 0

# for i in range(alunos): #o for vai percorrer alunos
#     media = 0
#     for j in range (notas): #percorrer notas
#         media += float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
#     media  /= notas
#     medias.append(media)
#     if media >= 7:
#         media_sete += 1
        
# print("\nA media dos alunos foi:")
# for i in range(alunos):
#     print(f"Aluno {i + 1}: {medias[i]}")
    
# print(f"\n{media_sete} alunos tiveram media maior ou igual a 7.")

"""
7 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a 
soma, a multiplicação e os números.
"""

# numeros_inteiros = [20,15,7,8,12]

# soma = sum(numeros_inteiros)
# print(f"Soma: {soma}")

# multiplicacao = 1
# for n in numeros_inteiros:
#     multiplicacao *= n
# print(f"Multiplicacao: {multiplicacao}")    

# print(f"Os numeros inteiros: {numeros_inteiros}")

"""
8 - Faça um Programa que peça a idade e a altura de 5 pessoas, 
armazene cada informação no seu respectivo vetor. Imprima a idade e 
a altura na ordem inversa a ordem lida.      
"""

# idade = []
# altura = []
# pessoas = 5

# for i in range(pessoas):
#     digitar_idade = int(input(f"Digite a idade da pessoa {i}:"))
#     digitar_altura = float(input(f"Digite a altura da pessoa {i}:"))
#     idade.append(digitar_idade)
#     altura.append(digitar_altura)
   
# # Ordem Lida
# print(f"\n============ Ordem lida ============")

# print(f"\nAs idades informadas das pessoas: {idade}")
# print(f"As alturas informadas das pessoas: {altura}")

# #Ordem Inversa
# idade.sort(reverse=True)
# altura.sort(reverse=True)
# print(f"\n=========== Ordem inversa ==========")

# print(f"\nAs idades informadas das pessoas: {idade}")
# print(f"As alturas informadas das pessoas: {altura}")

"""
9 - Faça um Programa que leia um vetor A com 10 números 
inteiros, calcule e mostre a soma dos quadrados dos 
elementos do vetor.
"""

# vetor_A = [20,45,3,46,11,2,90,77,9,10]

# print(f"Os numeros guardados dentro do Vetor A: \n{vetor_A}")
# print("----------------------------------------")
# #Calculo:

# soma = sum(vetor_A)
# print(f"A soma dos itens do vetor sao: {soma}")

"""
10 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere 
um terceiro vetor de 20 elementos, cujos valores deverão ser compostos 
pelos elementos intercalados dos dois outros vetores.      
"""

# vetor_1 = [0,5,8,10,2,34,45,22,3,1]
# vetor_2 = [11,10,20,2,56,7,101,67,90,87]
# vetor_3 = []

# print(f"Elementos do vetor 1: \n{vetor_1}")
# print(f"Elementos do vetor 2: \n{vetor_2}")

# vetor_1.extend(vetor_2)
# vetor_3.append(vetor_1)
# print(f"Os dois vetores dentro do vetor 3: \n{vetor_3}")