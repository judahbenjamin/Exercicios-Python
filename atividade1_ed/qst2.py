#ESTRUTURA DE DADOS
#DATA: 20/08/2024
#JUDAH BENJAMIN

# 2. Crie um programa que deverá imprimir todos os números ímpares inteiros de 20 até 100.

from time import sleep
cont = 20

print("Contagem de 20 a 100:")
while cont < 101:
    sleep(0.15)
    cont+=1
    if cont % 3 == 0:
        print(cont)

print("PROGRAMA FINALIZADO...")