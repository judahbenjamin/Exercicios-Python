#LÓGICA DE PROGRAMAÇÃO E ALGORITMO
#PROF: MÁRCIO CLAY
#ALUNO: JUDAH BENJAMIN
#DATA: 02/04/2024
#LISTAS PYTHON

#Lista é uma coleção ordenada e mutável. Permite membros duplicados.

thislist = ["apple","banana","cherry"]
print(thislist)

#Permite duplicatas

thislist = ["apple","banana","cherry","apple","cherry"]
print(thislist)

#Comprimento da lista

thislist = ["Goiaba","banana","laranja"]
print(len(thislist))

#Tipos de dados de lista

list1 = ["Maca","Jaca","Manga"]
list2 = [1,5,7,9]
list3 = [True, False, False, True]

print(type(list1))
print(type(list2))
print(type(list3))
print(type(list1[0]))
print(type(list2[1]))
print(type(list3[2]))

#Construtor List

lista = list(("Apple",35,True))
print(lista)
