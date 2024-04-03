#LOGICA DE PROGRAMAÇÃO E ALGORITMO
#PROFESSOR: MÁRCIO CLAY
#ALUNO: JUDAH BENJAMIN
#DATA: 03/04/2024
#PYTHON LISTS

print("============= ACESSAR ITENS DE UMA LISTA ==============")

frutas = ["Banana","Maca","Manga"]
print(frutas[1])

#ACESSANDO OS ULTIMOS ITENS DA LISTA(NEGATIVE INDEX)

frutas = ["Banana","Maca","Manga"]
print(frutas[-1])
print(frutas[-2])


#GAMA DE ÍNDICES(INTERVALO)


frutas = ["Banana","Maca","Manga","Laranja","Kiwi","Caju","Maracuja"]
print(frutas[2:6])

#OMITIR VALOR INICIAL

frutas = ["Banana","Maca","Manga","Laranja","Kiwi","Caju","Maracuja"]
print(frutas[:4])

#OMITIR VALOR FINAL

frutas = ["Banana","Maca","Manga","Laranja","Kiwi","Caju","Maracuja"]
print(frutas[4:])


#GAMA DE ÍNDICES NEGATIVOS(INTERVALO)

frutas = ["Banana","Maca","Manga","Laranja","Kiwi","Caju","Maracuja"]
print(frutas[-4:-1])

#VERIFICAR SE O ITEM EXISTE

frutas = ["Banana","Maca","Manga"]
if "Banana" in frutas:
    print("Positivo")

print("============= ALTERAR ITENS DE UMA LISTA ==============")

frutas = ["Banana","Maca","Manga"]
frutas[1] = "Morango"
print(frutas)

#ALTERAR INTERVALO

frutas = ["Banana","Maca","Manga","Laranja","Kiwi","Caju","Maracuja"]
frutas[1:3] = ["Morango","Abacate"]
print(frutas)

frutas = ["Banana","Maca","Manga"]
frutas[1:3] = ["Melancia"]
print(frutas)

print("============= ADICIONAR ITENS DE UMA LISTA ==============")

#ANEXAR ITENS (APPEND())
frutas = ["Banana","Maca","Manga"]
frutas.append("Maracuja")
print(frutas)

#INSERIR ITENS (INSERT())

frutas = ["Banana","Maca","Manga"]
frutas.insert(1,"Maracuja")
print(frutas)

#ESTENDER LISTA (EXTEND())

frutas1 = ["Banana","Maca","Manga"]
frutas2 = ["Caju","Maracuja","Laranja"]
frutas1.extend(frutas2)
print(frutas1)

#O EXTEND PODE ANEXAR QUALQUER OBJETO

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print("============= REMOVER ITENS DE UMA LISTA ==============")

#REMOVER ITEM ESPECIFICADO (REMOVE())

frutas = ["Banana","Maca","Manga"]
frutas.remove("Banana")
print(frutas)

#REMOVE A PRIMEIRA OCORRENCIA

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#REMOVER INDICE ESPECIFICADO (POP())

frutas = ["Banana","Maca","Manga"]
frutas.pop(2)
print(frutas)

frutas = ["Banana","Maca","Manga"]
frutas.pop()
print(frutas)

#A PALAVRA DEL TAMBEM REMOVE O INDICE ESPECIFICADO

frutas = ["Banana","Maca","Manga"]
del frutas [0]
print(frutas)

#DEL PODE EXCLUIR COMPLETAMENTE A LISTA

frutas = ["Banana","Maca","Manga"]
del frutas

#LIMPAR A LISTA (CLEAR())

frutas = ["Banana","Maca","Manga"]
frutas.clear()
print(frutas)

print("============= LISTAS DE LOOPS ==============")

#PERCORRER UMA LISTA (FOR)

frutas = ["Banana","Maca","Manga"]
for x in frutas:
    print(x)
    
#PERCORRER OS NUMEROS DE INDÍCE

frutas = ["Banana","Maca","Manga"]
for i in range(len(frutas)):
    print(frutas[i])
    
#USANDO O WHILE

frutas = ["Banana","Maca","Manga"]

i = 0

while i < len(frutas):
    print(frutas[i])
    i = i + 1
    
#LOOP USANDO COMPREENSÃO DE LISTA

frutas = ["Banana","Maca","Manga"]
[print(x) for x in frutas]