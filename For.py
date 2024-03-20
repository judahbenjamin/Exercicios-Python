#LÓGICA E ALGORITMO DE PROGRAMAÇÃO
#JUDAH BENJAMIN
#DATA: 20/03/2024
#ESTRUTURA FOR

#FOR - estrutura de controle que permite executar um bloco de código para cada elemento de uma sequência

#Estruturas de dados básicas em Python
# 1- Listas
# 2 - Tuplas
# 3 - Dicionários
# 4 - Conjuntos


#Exemplo #01

x = 0

for x in range(5):
    print("Ola, Mundo!")
    
#Exemplo #02

times = ["Flamengo","Corinthias","Palmeiras"]
for x in times:
    print(times)
    
#Exemplo #03

lista_frutas = ["Maca","Banana","Laranja","Uva"]

for fruta in lista_frutas:
    print(f"Eu gosto de comer {fruta}.")
    
#Exemplo #04

numero = 1

while numero <= 10:
    for i in range (2, numero):
        if numero % i == 0:
            break
    else:
        print(f"{numero} e primo.")
    numero += 1
    
#Exemplo #05

for x in range(3):
    nome = input("Digite seu nome: ")
    cpf = int(input("Digite seu cpf: "))
    print(f"O nome e {nome} e cpf {cpf}")