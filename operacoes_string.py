#EXERCÍCIO OPERAÇÕES COM STRINGS
#POR JUDAH BENJAMIN
#DATA: 14/10/24

"""
1. Crie um programa que deverá receber uma string e que deverá exibir essa string
invertida. Atenção: a string deve ser armazenada invertida na variável antes de ser
exibida.
"""

# string = input("Digite uma string: ")

# string_invertida = ''.join(reversed(string))
# print(string_invertida)

"""
2. Crie um programa que deverá receber uma string e deverá informar a quantidade de
caracteres que a string recebida tem. O programa deverá informar a quantidade com
espaços e também sem os espaços. 
"""

# def olhar_espaco(string):
#     count = 0
#     for i in range(0, len(string)):
#         if string[i] == " ":
#             count += 1 
 
#     return count

# string = input("Digite uma string: ")
# tamanho_caracteres = len(string)
# semcarac = len(string.replace(" ",""))

# print(f"Quantidade de caracteres da string e: {tamanho_caracteres}")
# print(f"O numero de espacos e: {olhar_espaco(string)}")
# print(f"O numero de sem espacos e: {semcarac}")

"""
3. Crie um programa que deverá receber uma string e deverá informar quantas vogais
(a, e, i, o, u) existem na string recebida. O programa deverá exibir a string obtida ao
final.
"""

# string = input("Digite um texto: ")

# vogais = []

# for i in string:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         vogais.append(i)

# print(f"Texto digitado: {string}")
# print(f"O texto tem {len(vogais)} vogais")

"""
4. Crie um programa que deverá receber uma string e deverá substituir todos os
caracteres “a” pelo caractere “x”. O programa deverá exibir a string obtida ao final.   
"""

# string = input("Digite uma string: ")
# i = 0

# for i in string:
#     if i == 'A' or i == 'a':
#         subs_carac = string.replace(i,"X")
        
# print(f"A string substituida ficou: {subs_carac}")

"""
5. Crie um programa que deverá receber uma string(uma frase) e deverá contar o
número de palavras contidas nela. O programa deverá exibir o número obtido ao
final. 
"""

# frase_string = input("Digite uma frase: ")

# palavras = frase_string.split()
# contagem_palavras = len(palavras)
# print(f"Contagem das palavras: {contagem_palavras}")

"""
6. Crie um programa que deverá receber uma string e que deverá converter a primeira
letra de cada palavra da frase para a letra maiúscula. O programa deverá exibir a
string obtida ao final.  
"""

# string = input("Digite uma string: ")
# p = ['da', 'de', 'di', 'do', 'du', 'para']

# def inicial_maiusculo(string):
#     items = []
#     for item in string.split():
#         if not item in p:
#             item = item.capitalize()
#         items.append(item)
#     return ' '.join(items)

# print(f"Resultado: {inicial_maiusculo(string)}")

"""
7. Crie um programa que deverá receber uma string e que esse programa seja capaz
de remover todos os espaços em branco da string recebida. O programa deverá
exibir a string obtida ao final.  
"""

# i = 0
# string = input("Digite uma string: ")

# for i in string:
#     if i == " ":
#         remover_espacos = string.replace(" ","")
# print(f"Resultado da string: {remover_espacos}")

"""
8. Crie um programa que deverá receber duas strings e que deverá comparar as duas
strings, o programa deverá informar se as duas strings são iguais ou não. Atenção:
O programa deve ignorar a condição de caixa alta ou caixa baixa.
"""

# string1 = input("Digite a 1° palavra: ")
# string2 = input("Digite a 2° palavra: ")

# if string1.lower() == string2.lower():
#     print("SAO IGUAIS!")
# elif string1.upper() == string2.upper():
#     print("SAO IGUAIS")
# else:
#     print("SAO DIFERENTES!")