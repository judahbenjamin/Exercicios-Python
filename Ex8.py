#LÓGICA E ALGORITMO DE PROGRAMAÇÃO
#PROF: MARCIO CLAY
#ALUNO: JUDAH BENJAMIN
#DATA: 05/03/2024
#EXERCÍCIOS 


#fstring - como incluir uma variavel dentro do texto. Maneira profissional.

"""
numero = int(input("Digite um numero:"))
print(f"O numero informado foi: {numero}")

se não usasse fstring

numero = int(input("Digite um numero:"))
print("O numero informado foi:",numero)
"""

"""
nome = "Judah"
idade = 18
estudo = "programacao"

print(f"Meu nome e {nome}, tenho {idade} anos e estudo {estudo}")
"""

"""
n_inteira = int(input("Digite um numero:"))
print(n_inteira*1)
print(n_inteira*2)
print(n_inteira*3)
print(n_inteira*4)
print(n_inteira*5)
print(n_inteira*6)
print(n_inteira*7)
print(n_inteira*8)
print(n_inteira*9)
print(n_inteira*10)
"""

"""
1 - Escreva um algoritmo em PORTUGOL para determinar se um dado número N (recebido através do teclado)
é POSITIVO, NEGATIVO, OU NULO.
"""

#Number = int(input("Digite um numero:"))

#if Number > 0:
    #print("O numero e POSITIVO")
#elif Number == 0:
    # print("O numero e NULO")
#else:
    #print("O numero e NEGATIVO")
  
    
"""
 2 - Faça um algoritmo que leia um número N e imprima F1,F2 ou F3, conforme a condição:
F1, se N <= 10, -F2, se N > 10 e N <=100 e   F3, se n > 100.
"""

#N = int(input("Digite um numero:"))

#if N <= 10:
    #print("F1")
#elif N > 10 and N <=100:
    #print("F2")
#else:
   # print("F3")
    
    
"""
3 - Construa um algortimo que receba como entrada tres valores e os imprima em ordem crescente.   
"""

"""N1 = int(input("Digite o primeiro numero:"))
N2 = int(input("Digite o segundo numero:"))
N3 = int(input("Digite o terceiro numero:"))

if N1 > N2 and N1 > N3 and N2 > N3:
    print(f"A ordem crescente e: {N3},{N2},{N1}")
elif N2 > N1 and N2 > N3 and N3 < N1:
    print(f"A ordem crescente e: {N3}, {N1}, {N2}")
elif N2 > N1 and N2 > N3 and N3 > N1:
    print(f"A ordem crescente e: {N1}, {N3}, {N2}")
elif N2 > N1 and N2 < N3 and N3 > N1:
    print(f"A ordem crescente e: {N1}, {N2}, {N3}")
elif N2 < N1 and N2 < N3 and N3 > N1:
    print(f"A ordem crescente e: {N2}, {N1}, {N3}")
else:
    print(f"A ordem crescente e: {N2},{N3},{N1}")
""" 
"""
4 - Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a 
possuir o valor de B e a variável de B passe a possuir o valor da variável A. Apresentar os valores trocados.   
"""

#A = input("Digite um valor a:")
#B = input("Digite um valor b:")

#Aux = A
#A = B
#B = Aux

#print(f"O valor de A vai ser: {A}")
#print(f"O valor de B vai ser: {B}")

"""
5 - Ler dois numeros e informar qual e o maior e qual e o menor.
"""

"""
n1 = int(input("Digite o numero 1:"))
n2 = int(input("Digite o numero 2:"))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

print(f"O numero maior e {maior}")
print(f"O numero menor e {menor}")
"""

"""
6 - Considere que o último concurso vestibular apresentou três provas: Português, Matemática e Conhecimentos Gerais.
Considerando que para cada candidato tem-se um registro contendo o seu nome e as notas obtidas em cada uma das provas,
construa um algoritmo que forneça:

a) o nome e as notas em cada prova do candidato
b) a média do candidato
c) uma informação dizendo se o candidato foi aprovado ou não. Considere que um candidato é aprovado se sua média for
maior que 7.0
"""

nome = input("Nome do candidato:")
portugues = float(input("Nota em portugues:"))
matematica = float(input("Nota em matematica:"))
conh_gerais = float(input("Nota em conhecimento gerais:"))

media = (portugues + matematica + conh_gerais)/3

if media >= 7:
    print("O candidato foi aprovado.")
else:
    print("O candidato foi reprovado.")