#EXERCICIOS PYHTON
#REVISÃO
#JUDAH BENJAMIN
#DATA: 11/03/2024

"""
1 - Escreva um algoritmo em PORTUGOL para determinar se um dado numero N (recebido atraves do teclado)
é POSITIVO, NEGATIVO e NULO.
"""

"""
Num = int(input("Digite um numero:"))

if Num > 0 :
    print("O numero e POSITIVO.")
elif Num == 0 :
    print("O numero e NULO.")
else:
    print("O numero e NEGATIVO.")
"""

""" 
2 - Construa um algoritmo que receba como entrada tres valores e os imprima em ordem crescente.
"""

"""
n1 = float(input("Digite o primeiro valor:"))
n2 = float(input("Digite o segundo valor:"))
n3 = float(input("Digite o terceiro valor:"))

if n1 > n2 and n1 > n3 and n2 > n3:
    print(f"A ordem crescente e: {n3},{n2},{n1}")
elif n2 > n1 and n2 > n3 and n3 < n1:
    print(f"A ordem crescente e: {n3},{n1},{n2}")
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(f"A ordem crescente e: {n1},{n3},{n2}")
elif n2 > n1 and n2 < n3 and n3 > n1:
    print(f"A ordem crescente e: {n1},{n2},{n3}")
elif n2 < n1 and n2 < n3 and n3 > n1:
    print(f"A ordem crescente e: {n2},{n1},{n3}")
else:
    print(f"A ordem crescente e: {n2}, {n3}, {n1}")
      
  """

#Troca de valores

"""
a = int(input("Digite um valor de A:"))
b = int(input("Digite um valor de B:"))

aux = a
a = b
b = aux

print(f"O valor de A sera {a}")
print(f"O valor de b sera {b}")
"""

"""
3 - Considere que o último concurso de vestibular apresentou três provas: Português, Matemática, e Conhecimentos gerais.
Considerando que para cada candidato tem-se um registro contendo o seu nome e as notas obtidas em cada uma das provas, 
construa um algoritmo que forneça:

a - o nome e as notas em cada prova do candidato
b -  a media do candidato
c - uma informação dizendo se o candidato foi aprovado ou não. Considere que um candidato é aprovado se sua media for
mairo que 7.0.    
"""

"""
nome = input("Digite o nome do candidato:")
nota_portugues = float(input("Digite a nota do candidato em portugues:"))
nota_matematica = float(input("Digite a nota do candidato em matematica:"))
nota_conhecimentos_gerais = float(input("Digite a nota do candidato em conhecimentos gerais:"))

media = (nota_portugues + nota_matematica + nota_conhecimentos_gerais)/3

print("///////////////////// RESULTADO ///////////////////////")

if media >= 7.0:
    print(f"O(a) {nome} foi aprovado.")
    print(f"Media:{media:.2f}")
else:
    print(f"O(a) {nome} foi reprovado.")
    print(f"Media:{media:.2f}") 
"""

#fstrings  
    
Nome = "Judah"
Profissao = "Estudante"
Idade = 18
Sonho = "Futuro programador e técnico em informática."

print(f"Olá, meu nome e {Nome}! Sou {Profissao}, tenho {Idade} anos.")
print(f"Pretendo ser um {Sonho}")


