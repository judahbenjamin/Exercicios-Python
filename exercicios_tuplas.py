#LÓGICA DE PROGRAMAÇÃO EXERCICIOS TUPLAS
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

# from random import randint
# numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
# print("Os valores sorteados: ", end="")

# for n in numeros:
#     print(f"{n} ", end="")
# print(f"\nO maior valor sorteado foi: {max(numeros)}")
# print(f"O menor valor sorteado foi: {min(numeros)}")

"""
4 - Desenvolva um programa que leia quatro valores pelo teclado e
guarde-os em uma tupla. No final, mostre:
    ● Quantas vezes apareceu o valor 9
    ● Em que posição foi digitado o valor 3
    ● Quais foram os números pares
"""

# valores = []

# cont = 0

# while cont < 4:
#     valor = int(input("Digite um valor: "))
#     valores.append(valor)
#     cont += 1

# valores2 = tuple(valores)
# print(f"Os valores guardados na tupla: {valores2}")

# quantidade = valores2.count(9)
# print(f"O valor 9 apareceu {quantidade} vez")

# if 3 in valores2:
#     print(f"O valor 3 apareceu na {valores2.index(3)+1} posicao")

# print("Os valores pares foram: ", end='')
# for num in valores2:
#     if num % 2 == 0:
#         print(num, end=' ')

"""
5 - Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final mostre uma listagem de
preços organizando os dados em forma tabular.  
"""

# from tabulate import tabulate

# dados = (
#     ("Nome do produto", "Preco"),
#     ("Arroz", 25.95),
#     ("Feijao", 30.00),
#     ("Macarrao", 20.95),   
#     ("Bombrio", 10.00),   
#     ("Banana", 12.00), 
# )
  
# tabela = tabulate(dados, headers="firstrow", tablefmt="grid")
# print(tabela)

"""
6 - Crie um programa que tenha uma tupla com várias palavras ( não usar
acentos ). Depois disso, você deve mostrar para cada palavra quais são as
suas vogais. 
"""

# palavras = ("Cachorro","Gato","Carro","Tijela","Garfo","Caminhao",
#             "Jato","Pizza","Biscoito","Cavalo","Jegue","Mato","Jogo",
#             "Musica","Perigo","Atencao","Mingau","Escola","Programar")

# for p in palavras:
#     print(f"\nNa palavra {p.upper()} temos as seguintes vogais: ", end='')
#     for letra in p:
#         if letra.lower() in 'aeiou':
#             print(letra, end=' ')

        



