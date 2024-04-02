#LÓGICA DE PROGRAMAÇÃO E ALGORITMO
#PROF: MÁRCIO CLAY
#ALUNO: JUDAH BENJAMIN
#DATA: 02/04/2024
#LISTAS PYTHON EXERCÍCIOS

#01 - CRIAR UMA LISTA COM NOMES
# IMPRIMIR NA TELA A QTD DE VALORES NA LISTA
# IMPRIMIR O ITEM 2 DA LISTA
# IMPRIMIR O TIPO DE DADO DESTA LISTA

lista_alunos = ["Judah","Adenilton","Linda Ines","Joao"]
print(f"Quantidade de alunos: {len(lista_alunos)}")
print(f"Item 2 da lista: {lista_alunos[1]}")
print(f"Tipo de dado da lista: {type(lista_alunos)}")
print(f"Valores da lista: {lista_alunos}")
print(f"Tipos de dados de um dos valores da lista: {type(lista_alunos[0])}")

#02 - Escreva  um  programa  que  receba  uma  lista  de  10  inteiros  via  teclado  e imprima todo a lista em na mesma linha. 

#lista_numeros = [1,22,4,5,67,90,9,3,55,15]
#print(lista_numeros)

"""
numero1 = int(input("Digite o primeiro numero:"))
numero2 = int(input("Digite o segundo numero:"))
numero3 = int(input("Digite o terceiro numero:"))
numero4 = int(input("Digite o quarto numero:"))
numero5 = int(input("Digite o quinto numero:"))
numero6 = int(input("Digite o sexto numero:"))
numero7 = int(input("Digite o setimo numero:"))
numero8 = int(input("Digite o oitavo numero:"))
numero9 = int(input("Digite o nono numero:"))
numero10 = int(input("Digite o decimo numero:"))
list_num = [numero1,numero2,numero3,numero4,numero5,numero6,numero7,numero8,numero9,numero10]
print(f"Lista dos numeros inteiros: {list_num}")  
"""

#03 - Escreva um programa que receba uma lista de 10 inteiros via teclado, em seguida  o  
# programa  deve  solicitar  um  número  e  informar  se  o  número também está na lista ou não.

"""
numero1 = int(input("Digite o primeiro numero:"))
numero2 = int(input("Digite o segundo numero:"))
numero3 = int(input("Digite o terceiro numero:"))
numero4 = int(input("Digite o quarto numero:"))
numero5 = int(input("Digite o quinto numero:"))
numero6 = int(input("Digite o sexto numero:"))
numero7 = int(input("Digite o setimo numero:"))
numero8 = int(input("Digite o oitavo numero:"))
numero9 = int(input("Digite o nono numero:"))
numero10 = int(input("Digite o decimo numero:"))
list_num = [numero1,numero2,numero3,numero4,numero5,numero6,numero7,numero8,numero9,numero10]
print(f"Lista dos numeros inteiros: {list_num}")

solicitar = input("Digite algum numero da lista:")
pergunta = int(input("O numero esta na lista(Sim - 1, Nao - 0):"))

if pergunta == 1:
    print("O numero esta na lista")
else:
    print("Incorreto")      
"""
