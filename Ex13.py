#LÓGICA DE PROGRAMAÇÃO E ALGORITMO
#JUDAH BENJAMIN
#DATA: 19/03/2024
#EXERCICIOS WHILE

#EXEMPLO #01

i = 0

while i <= 6:
    print(i)
    i += 1
    
    
#EXEMPLO #02

"""
    x = 0

while x < 3:
    nome = input("Digite o seu nome: ")
    cpf = int(input("Digite CPF: "))
    print(nome)
    print(cpf)
    x += 1

    print(f"Nome pessoa {x} = {nome}")
    print(f"CPF pessoa {x} = {cpf}")
    
    
 """
    
#EXEMPLO #03

"""
x = 1
soma = 0

while x <= 3:
    numero = int(input("Digite o 1° numero: "))
    soma = soma + numero
    print(f"A soma e {soma}")
    x += 1
"""

#EXEMPLO #04

"""
    numero = 1

    while numero < 5:
        numero1 = int(input("Digite o 1° numero: "))
        numero2 = int(input("Digite o 2° numero: "))
        soma = numero1 + numero2
    
        print("soma N° {} e: {}".format(numero, soma))
        print("====================================")
        numero += 1  
"""

#EXEMPLO #05

"""
    n = 1

    while n < 10:
        print("=================================")
        Nome = input("Digite o nome do candidato: ")
        Nota_portugues = float(input("Digite a nota de portugues: "))
        Nota_matematica = float(input("Digite a nota de matematica: "))
        Nota_conhecimento_gerais = float(input("Digite a nota em conhecimentos gerais: "))
    
        media = (Nota_portugues+Nota_matematica+Nota_conhecimento_gerais)/3
    
        print("Nome: {}".format(Nome))
        print("Media: {:.2f}".format(media))
    
        if media >= 7:
            print("O candidato foi APROVADO!")
        else:
            print("O candidato foi REPROVADO!")   

        print("=================================")
        n += 1
"""
    
#EXEMPLO #06

"""
    c = 1

    while c < 5:
        categoria_produtos = input(f"Digite a categoria {c}: ")
        l1 = input("Digite o produto 1:")
        l2 = input("Digite o produto 2:")
        l3 = input("Digite o produto 3:")
        l4 = input("Digite o produto 4:")
    
        print(f"categoria {c}:")
        lista = [l1, l2, l3, l4]
        print(lista)
        print("=====================================")
        c += 1

"""

#EXEMPLO #07
    
Num = 1

while Num <= 6:
    if Num % 2 == 0:
        print(f"O {Num} e PAR!")
    else:
        print(f"O {Num} e IMPAR!")
    Num += 1