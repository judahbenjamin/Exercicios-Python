#LÓGICA DE PROGRAMAÇÃO EXERCICIOS
#DATA: 21/05/2024

"""
1 - Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até 20. Seu programa deverá ler um número
pelo teclado entre 0 e 30 e mostrá-lo por extenso
"""

# contagem = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito",
#             "nove","dez","onze","doze","treze","quatorze","quinze","dezesseis",
#             "dezessete","dezoito","dezenove","vinte")

# numero = int(input("Digite um numero: "))

# if numero >= 0 and numero <= 20:
#     print(f"O numero digitado: {numero}")
#     print(f"O numero em extenso: {contagem[numero]}")
# else:
#     print("Numero nao encontrado!")

"""
2 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do
campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
    ● Apenas os 5 primeiros colocados
    ● Os últimos 4 colocados da tabela
    ● Uma lista com os times em ordem alfabética
    ● Em que posição na tabela está o time da chapecoense
"""

# os_colocados = ("Athletico-PR","Bahia","Flamego","Botafogo","Sao Paulo","Cruzeiro","Atletico-MG","Bragantino",
#                 "Palmeiras","Internacional","Fortaleza","Gremio","Vasco da Gama","Criciuma","Juventude","Corinthias",
#                 "Fluminense","EC Vitoria","Atletico-GO","Chapecoense")

# print("Os 5 primeiros colocados:")
# print(os_colocados[:5])

# print("Os ultimos 4 colocados da tabela:")
# print(os_colocados[-4:])

# #Convertendo tupla em lista
# campeonato = list((os_colocados))
# print(campeonato)

# print("Em ordem alfabetica:")
# campeonato.sort()
# print(campeonato)

# print(f"Posicao do Chapecoense: {os_colocados.index("Chapecoense")}")

"""3 - Crie um programa que vai gerar cinco números aleatórios e colocar em
uma tupla. Depois disso mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
"""
# numeros = []

# cont = 0

# while cont < 5:
#     num = int(input("Digite um numero:"))
#     cont += 1
#     numeros.append(num)
# print(numeros)

# numeros2 = tuple((numeros))
# print(f"Tupla: {numeros2}")



