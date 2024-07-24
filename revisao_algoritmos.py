#REVISAO DE ALGORITMOS

# 1 – Faça um programa que leia 10 números e informe:
# a)	A soma destes números;
# b)	A média destes números;
# c)	O maior número; e
# d)	O menor número.

# numeros = [10,2,4,55,3,90,11,22,5,12]
# print(f'Lista dos numeros: {numeros}')

# soma = sum(numeros)
# print(f'A soma dos numeros: {soma}')

# media = sum(numeros)/len(numeros)
# print(f'A media dos numeros: {media}')

# maior = max(numeros)
# print(f'O maior numero: {maior}')

# menor = min(numeros)
# print(f'O menor numero: {menor}')

# 2 – Faça um programa que leia o nome, idade e sexo de várias pessoas até que o nome digitado seja “FIM” e informe:
# a)	O nome e a idade da pessoa mais velha;
# b)	O nome e a idade da pessoa mais nova;
# c)	Quantas pessoas eram do sexo masculino;
# d)	Quantas pessoas eram do sexo feminino; e
# e)	A quantidade de pessoas digitadas e a média de idade.


while True:
    nome = input('NOME: ')
    idade = int(input('IDADE: '))
    sexo = input('SEXO: ')
    print('='*30) 
    
    if nome == 'fim':
        break
    
# 3 – Faça um programa que leia o número e o peso de um boi, a leitura encerra quando o número digitado for 0 (zero) e informe:
# a)	Quantos bois foram digitados;
# b)	Qual o total de peso dos bois;
# c)	Qual a média de peso dos bois;
# d)	Qual o número e o peso do boi mais pesado; e
# e)	Qual o número e o peso do boi mais leve.
