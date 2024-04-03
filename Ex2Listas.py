#LOGICA DE PROGRAMAÇÃO E ALGORITMO
#PROFESSOR: MÁRCIO CLAY
#ALUNO: JUDAH BENJAMIN
#DATA: 03/04/2024
#EXERCICIOS LISTAS 2

#EXERCICIO 1

"""
alunos = []

quantidade_alunos = int(input("Digite a quantidade de alunos: "))

for x in range(quantidade_alunos):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    
print("Lista dos alunos: {}".format(alunos))   
"""

"""
alunos = []

quantidade_alunos = int(input("Digite a quantidade de alunos: "))

for x in range(quantidade_alunos):
    nome = input("Digite o nome do aluno: ")
    posicao = int(input("Digite a posicao:"))
    alunos.insert(posicao,nome)
    
print("Lista dos alunos: {}".format(alunos))    
"""

#EXERCICIO 2 - SOMAR ITENS

numeros = []
soma = 0

quantidade_soma = int(input("Digite a quantidade de itens: "))

for c in range(quantidade_soma):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
    soma = soma + numero
    
print(f"A soma dos itens e: {soma}")

#EXERCICIO 3 - EXCLUIR ITENS DA LISTA
#EXERCICIO 4 - MESCLAR ITENS
#EXERCICIO 5 - VERIFICAR SE UM "ALUNO" ESTA NA LISTA

