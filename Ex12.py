#EXERCICIOS
#DATA: 12/03/2024
#JUDAH BENJAMIN

"""
1 - Ler dois numeros e informar qual e maior e menor.  
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



