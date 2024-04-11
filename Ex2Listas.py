#LOGICA DE PROGRAMAÇÃO E ALGORITMO
#PROFESSOR: MÁRCIO CLAY
#ALUNO: JUDAH BENJAMIN
#DATA: 04/04/2024
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

"""
numeros = []
soma = 0

quantidade_soma = int(input("Digite a quantidade de itens: "))

for c in range(quantidade_soma):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
    soma = soma + numero
    
print(f"A soma dos itens e: {soma}")  
"""

#EXERCICIO 3 - EXCLUIR ITENS DA LISTA

"""
alunos_list = []

lista_de_alunos = int(input("Digite a quantidade de alunos: "))

for x in range(lista_de_alunos):
    nome = input("Digite o nome do aluno: ")
    alunos_list.append(nome)
    
print(f"Lista dos alunos: {alunos_list}")

remove = int(input("Remova algum nome da lista digitando o indice: "))
del(alunos_list[remove])
print(f"A lista: {alunos_list}")  
"""


#EXERCICIO 4 - MESCLAR ITENS

"""
capital = ["Vila Velha","Sao Paulo","Belo Horizonte"]
estado = ["ES","SP","MG"]
capital.extend(estado)
print(capital)
"""

"""
capital = []
estado = []

lista_capital = int(input("Digite a quantidade de vezes: "))

for i in range(lista_capital):
    nome_capital = input("Digite o nome da capital: ")
    capital.append(nome_capital)

print(capital)

lista_estado = int(input("Digite a quantidade de vezes: "))

for e in range(lista_estado):
    nome_estado = input("Digite o nome do estado: ")
    estado.append(nome_estado)
    
print(estado)    

capital.extend(estado)
print(f"Mesclado: {capital}")    
"""
    
#EXERCICIO 5 - VERIFICAR SE UM "ALUNO" ESTA NA LISTA
