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

# quant_bois = boi_pesado = boi_leve = 0
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
    
#     for p in bois:
#         numero, peso = p
#         boi_pesado = max(pesos)
#         boi_leve = min(pesos)
        
#     # if cont == 0:
#     #     boi_pesado = peso
#     #     num_pesado = numero
#     #     boi_leve = peso
#     #     num_leve = numero

#     # if peso > boi_pesado:
#     #     boi_pesado = peso
#     #     num_pesado = numero
        
#     # if peso < boi_pesado:
#     #     boi_leve = peso
#     #     num_leve = numero
    
#     if answ == 0:
#         break
     
# print(f'A quantidade de bois foi {quant_bois}')
# print(f'O total de peso dos bois e: {sum(pesos)}')
# print(f'A media de peso dos bois e: {sum(pesos)/quant_bois:.2f}')
# print(f'O peso do boi mais pesado e {boi_pesado}, o numero e {numero}')
# print(f'O peso do boi mais leve e {boi_leve}, o numero e {numero}')


# 4 – Faça um programa que gere um vetor de 10 posições para números inteiros, preencha o vetor com números diversos, organize o vetor do menor para o maior e mostre:
# a)	O vetor digitado originalmente;
# b)	O vetor organizado do menor para o maior;

