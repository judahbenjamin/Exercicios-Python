#LÓGICA DE PROGRAMAÇÃO E ALGORITMO
#PROF: MÁRCIO CLAY
#ALUNO: JUDAH BENJAMIN
#DATA: 08/03/2024
#LISTA DE EXERCÍCIOS 02

"""
1 - Faça um programa que verifique (usando if e else) se uma letra digitada é vogal ou consoante. 
"""

#letra = input("Digite uma letra:")

#if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or \
   #letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
   #    print("Vogal")
#else:
    #print("Consoante")
   
   
"""
2 - Faça um programa para a leitura de duas notas parciais de um aluno. 
A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez;
A mensagem “Reprovado” se a média for menor de do que sete.
""" 

"""
Nota1 = 10.0
Nota2 = 10.0

Media = (Nota1 + Nota2)/2

if Media >= 7:
    print("Aprovado.")
elif Media == 10:
    print("Aprovado com distinção.")
else:
    print("Reprovado.")
"""
    
    
"""
3 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre o mais barato
"""

"""
preco_prod1 = float(input("Digite o preco do primeiro produto: "))
preco_prod2 = float(input("Digite o preco do segundo produto: "))
preco_prod3 = float(input("Digite o preco do terceiro produto: "))

if preco_prod1 < preco_prod2 and preco_prod3 and preco_prod1:
    print("O produto 1 e o mais barato.")
elif preco_prod2 < preco_prod1 and preco_prod3:
    print("O produto 2 e o mais barato.")
elif preco_prod3 < preco_prod1 and preco_prod2:
    print("O produto 3 e o mais barato.")

#Se alguns numeros forem iguais

elif preco_prod1 == preco_prod2 and preco_prod1 and preco_prod2 < preco_prod3:
    print("O produto 1 e 2 sao os mais baratos.")
elif preco_prod1 == preco_prod3 and preco_prod1 and preco_prod3 < preco_prod2:
    print("O produto 1 e 3 sao os mais baratos.")
elif preco_prod2 == preco_prod3 and preco_prod2 and preco_prod3 < preco_prod1:
    print("O produto 2 e 3 sao os mais baratos.")

#Se todos os numeros forem iguais

else:
    print("Todos os precos sao iguais.")
"""

"""
4 - As organizações CSM resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para 
desenvolver o programa que calculará os reajustes. 

 a. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual;

 b. Salários até R$ 280,00 (incluindo): aumento de 20%;
 c. Salários entre R$ 280,00 e R$700,00: aumento de 15%;
 d. Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%;
 e. Salários de R$ 1500,00 em diante: aumento de 5%

 Após o aumento ser realizado; informe na tela;
 a. O salário antes do reajuste;
 b. O percentual de aumento aplicado;
 c. O valor do aumento;
 d. O novo salário, após o aumento.
"""

salario = float(input("Salario do colaborador:"))

if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5
    
print("Salario original: R$ ", salario)
print("Percentual:", percentual,"%")

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento

print("Aumento: R$", aumento)
print("Novo salario: R$", novo_salario)


"""
5 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
 “Telefonou para a vítima? “
 “Esteve no local do crime?”
 “Mora perto da vítima? “
 “Devia para a vítima? “
 “Já trabalhou com a vítima? “  

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder 
positivamente a 2 questões ela deve ser classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como 
“Assassino“. Caso contrário, ele será classificado como “Inocente“.
"""

"""
positivos = 0
resposta = input("Telefonou para a vitima? (S ou N):")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Esteve no local do crime? (S ou N):")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Mora perto da vitima? (S ou N):")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Devia para a vitima? (S ou N):")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Ja trabalhou com a vitima? (S ou N):")
if resposta.upper() == "S":
    positivos += 1
    
if positivos < 2:
    print("Inocente")
elif positivos == 2:
    print("Suspeita")
elif positivos < 5:
    print("Cumplice")
else:
    print("Assassino")  
"""