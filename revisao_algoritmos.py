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

# maior_idade = menor_idade = contador = quant_masc = quant_fem = tot_idade = 0
# nome_velho = ''
# nome_novo = ''

# while True:
#     nome = input('NOME: ')
#     idade = int(input('IDADE: '))
#     sexo = input('SEXO [M] ou [F]: ').upper()
#     while sexo not in 'MF':
#         sexo = input('Digite um valor válido para Sexo [M] ou [F]: ').upper()
    
#     if contador == 0:
#         maior_idade = idade
#         nome_velho = nome
#         menor_idade = idade
#         nome_novo = nome
        
#     if idade > maior_idade:
#         maior_idade = idade
#         nome_velho = nome
        
#     if idade < menor_idade:
#         menor_idade = idade
#         nome_novo = nome
        
#     if sexo == 'M':
#         quant_masc += 1
#     else:
#         quant_fem += 1
        
#     tot_idade += idade
#     contador += 1
    
#     resp = input('Digite FIM para terminar ou ENTER para continuar: ').upper()
#     if resp == 'FIM':
#         break
#     print()
    
# media = tot_idade/contador
# print()
# print('=-'*30)
# print()
# print(f'A pessoa mais velha e {nome_velho} e tem {maior_idade} anos')
# print(f'A pessoa mais nova e {nome_novo} e tem {menor_idade} anos')
# print(f'Quantidade de pessoas do sexo Masculino: {quant_masc}')
# print(f'Quantidade de pessoas do sexo Feminino: {quant_fem}')
# print(f'Quantidade de pessoas digitadas foram {contador} com media de {media:.2f} de idade')
    

# 3 – Faça um programa que leia o número e o peso de um boi, a leitura encerra quando o número digitado for 0 (zero) e informe:
# a)	Quantos bois foram digitados;
# b)	Qual o total de peso dos bois;
# c)	Qual a média de peso dos bois;
# d)	Qual o número e o peso do boi mais pesado; e
# e)	Qual o número e o peso do boi mais leve.

# quant_bois = 0
# pesos = []
# bois = []

# while True:
#     numero = int(input('NUMERO: '))
#     peso = float(input('PESO DO BOI: '))
#     pesos.append(peso)
#     quant_bois += 1
    
#     answ = int(input('Deseja continuar? (S - 1 ; N - 0) '))
#     bois.append([numero,peso])
#     print('=-'*30)
    
#     primeira_posicao = bois[0]
#     boi_leve = primeira_posicao[1]
#     num_leve = primeira_posicao[0]
#     boi_pesado = primeira_posicao[1]
#     num_pesado = primeira_posicao[0]

#     for p in bois:
#         numero, peso = p

#         if peso > boi_pesado:
#             boi_pesado = peso
#             num_pesado = numero
            
#         if peso < boi_pesado:
#             boi_leve = peso
#             num_leve = numero
        
#     if answ == 0:
#         break
     
# print(f'A quantidade de bois foi {quant_bois}')
# print(f'O total de peso dos bois e: {sum(pesos)}')
# print(f'A media de peso dos bois e: {sum(pesos)/quant_bois:.2f}')
# print(f'O peso do boi mais pesado e {boi_pesado}, o numero e {num_pesado}')
# print(f'O peso do boi mais leve e {boi_leve}, o numero e {num_leve}')


# 4 – Faça um programa que gere um vetor de 10 posições para números inteiros, preencha o vetor com números diversos, organize o vetor do menor para o maior e mostre:
# a)	O vetor digitado originalmente;
# b)	O vetor organizado do menor para o maior;

# count = 0
# inteiros = []

# while count < 10:
#     num = int(input(f"Posição {count} = "))
#     inteiros.append(num)
#     count += 1
# print()
# print('=-'*30)
# print(f'O vetor digitado originalmente: {inteiros}')
# inteiros.sort(reverse=False)
# print(f'O vetor organizado do menor para o maior: {inteiros}')

# 5 - Faça um programa que gere uma matriz de 3 x 3, que receba números aleatórios, organize esta matriz do maior para o menor e mostre:
# a)    A matriz digitada originalmente;
# b)    A matriz organizada do menor para o maior;
# c)    O maior valor da matriz;
# d)    A média dos números digitados na matriz.

# matriz = [[0,0,0],[0,0,0],[0,0,0]]

# for linha in range(0, 3):
#     for coluna in range(0, 3):
#         matriz[linha][coluna] = int(input(f'Digite um valor [{linha},{coluna}]: '))
# print('=-='*30)
# print(f'A matriz digitada originalmente:')
# print()
# for linha in range(0, 3):
#     for coluna in range(0, 3):
#         print(f'[{matriz[linha][coluna]:^5}]', end='')
#     print()
# print()
# print(f'A matriz organizada do menor para o maior:')
# print()

# for linha in range(0, 3):
#     for coluna in range(0, 3):
#         matriz.sort()
# print(matriz)
# print()
# print(f'O maior valor da matriz:')
# print()
# for linha in range(0, 3):
#     for coluna in range(0, 3):
#         max(matriz)
# print(matriz)
# print()
# print(f'A media dos numeros digitados na matriz:')
# print()
# for linha in range(0, 3):
#     for coluna in range(0, 3):
#         soma = sum(matriz)
#         media = soma/len(matriz)
# print(media)
