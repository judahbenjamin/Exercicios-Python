#LÓGICA DE PROGRAMAÇÃO E ALGORITMO
#PROFESSOR: MÁRCIO CLAY
#ALUNO: JUDAH BENJMAIN
#DATA: 17/04/2024

"""
1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.   
"""

vetor_numeros = [1,2,3,4,5]
print(f"Os numeros sao: {vetor_numeros}")

"""
2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

numeros_reais = [1.0,2.4,3.2,4.5,5.0,6.0,7.8,8.9,9.0,10.3]
numeros_reais.sort(reverse= True)
print(f"A inversao e: {numeros_reais}")

"""
3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = [6.0, 7.5, 9.7, 10.0]
print(f"As notas sao: {notas}")

soma = sum(notas)
media = soma/len(notas)
print(f"A media das notas e: {media}")

"""
4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

lista_caracteres = []
t = 1

while t <= 10:
    caracter = input("Digite o caracter: ")
    lista_caracteres.append(caracter)
    t += 1
    
print(f"Os caracteres: {lista_caracteres}")

posicoes = 0

if caracter == "a" and caracter == "e" and caracter == "i" and caracter == "o" and caracter == "u":
    print("Vogais")
    vogal = caracter
# elif caracter != "a" and caracter != "e" and caracter != "i" and caracter != "o" and caracter != "u":
else:
    print("Consoantes")
    consoante = caracter
   
   
    # for x in posicoes:
    #     posicoes == lista_caracteres
    #     consoantes = caracter[posicoes]
    #     print(f"As consoantes sao: {consoantes}")

    
