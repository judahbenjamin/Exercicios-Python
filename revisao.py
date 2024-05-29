"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente". 
 """


pergunta_1 = int(input('Telefonou para a vitima? [S = 1, N = 0] '))
pergunta_2 = int(input('Esteve no local do crime? [S = 1, N = 0] '))
pergunta_3 = int(input('Mora perto da vitima? [S = 1, N = 0] '))
pergunta_4 = int(input('Devia para a vitima? [S = 1, N = 0] '))
pergunta_5 = int(input('Ja trabalhou com a vitima? [S = 1, N = 0] '))

resultado = pergunta_1 + pergunta_2 + pergunta_3 + pergunta_4 + pergunta_5

if resultado == 2:
    print('SUSPEITA')
elif resultado >= 3 and resultado <= 4:
    print('CUMPLICE')
elif resultado == 5:
    print('ASSASSINO')
else:
    print('INOCENTE')