#LÓGICA DE PROGRAMAÇÃO E ALGORITMO
#PROFESSOR: MÁRCIO CLAY
#ALUNO: JUDAH BENJMAIN
#DATA: 24/04/2024

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

media_alunos = []
alunos = []
aluno = 0

for x in range(10):
    for c in alunos:
        aluno = input("Digite o nome do aluno:")
        for aluno in range(4):
            nota = float(input("Digite a nota desse aluno:"))
        resultado = sum(nota in aluno)
        print(resultado)
    alunos.append(aluno)
    
