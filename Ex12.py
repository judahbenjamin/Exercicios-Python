#EXERCICIOS
#DATA: 13/03/2024
#JUDAH BENJAMIN

"""
1 - Ler dois numeros e informar qual e maior e menor.  
"""

"""
N1 = int(input("Digite o primeiro numero:"))
N2 = int(input("Digite o segundo numero:"))

if N1 > N2:
    Numero_Maior = N1
    Numero_Menor = N2
else:
    Numero_Maior = N2
    Numero_Menor = N1
    
print(f"O Numero maior e {Numero_Maior}")
print(f"O Numero menor e {Numero_Menor}")

"""

"""
2 - Ler os anos de nascimento de duas pessoas e calcular suas idades. Imprimir o nome e a idade de cada 
uma e indicar qual é a maior nova.   
"""

"""
nome_p1 = input("Digite o nome da primeira pessoa:")
nascimento_p1 = int(input("Digite o ano de nascimento da primeira pessoa:"))

nome_p2 = input("Digite o nome da segunda pessoa:")
nascimento_p2 = int(input("Digite o ano de nascimento da segunda pessoa:"))

idade_p1 = 2024 - nascimento_p1
idade_p2 = 2024 - nascimento_p2

if idade_p1 > idade_p2:
    nome_mais_nova = nome_p1
    idade_mais_nova = idade_p1
else:
    nome_mais_nova = nome_p2
    idade_mais_nova = idade_p2
    
print(f"Nome Pessoa 1: {nome_p1}")
print(f"Idade Pessoa 1: {idade_p1}")

print(f"Nome Pessoa 2: {nome_p2}")
print(f"Idade Pessoa 2: {idade_p2}")

print(f"O nome da pessoa mais nova: {nome_mais_nova}")
print(f"A idade da pessoa mais nova: {idade_mais_nova}")
"""

"""
3 - Suponha que o conceito de um aluno seja determinado em função da sua nota. Suponha, também, que esta
nota seja um valor inteiro na faixa de 0 a 100, conforme a seguinte faixa:  

Nota            Conceito
0 a 49          Insuficiente
50 a 69         Regular
70 a 84         Bom
85 a 100        Ótimo

Crie um algoritmo que apresente o conceito e a nota do aluno.     
"""

nota = int(input("Digite a nota do aluno:"))

conceito = None

if nota >= 0 and nota <= 49:
    conceito = "Insuficiente"
elif nota >= 50 and nota <= 69:
    conceito = "Regular"
elif nota >= 70 and nota <= 84:
    conceito = "Bom"
elif nota >= 85 and nota <= 100:
    conceito = "Otimo"
else:
    raise ValueError("Nota invalida:" + str(nota))

print(f"Nota: {nota}")
print(f"Conceito: {conceito}")



