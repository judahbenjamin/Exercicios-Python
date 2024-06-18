#ALGORITMO E LÓGICA DE PROGRAMAÇÃO
#DATA: 18/06/2024
#JUDAH BENJAMIN

"""
1 - um de entrada e outro de sa´ıda. Cada linha do arquivo de entrada contem o nome de ´
uma pessoa e o seu ano de nascimento. O programa devera ler o arquivo de entrada e ´
gerar um arquivo de sa´ıda onde aparece o nome da pessoa seguida por uma string que
representa a sua idade.
• Se a idade for menor do que 18 anos, escreva “menor de idade”
• Se a idade for maior do que 18 anos, escreva “maior de idade”
• Se a idade for igual a 18 anos, escreva “entrando na maior idade”   
"""

# from datetime import date

# anoAtual = date.today().year

# with open("nomes.txt","w",encoding="UTF-8") as arquivo:
#     arquivo.write('Mauro Bastos 2001' + '\n')
#     arquivo.write('Tales Silva 1998' + '\n')
#     arquivo.write('Carla Ramos 2004' + '\n')
#     arquivo.write('Maria Santos 2008' + '\n')
    
# with open("nomes.txt","r",encoding="UTF-8") as arquivo:
#     leitura = arquivo.readlines()
    
# for line in leitura:
#     nome, sobrenome, ano = line.split() #Dividir as strings em índices
#     idade = anoAtual - int(ano)
#     mensagem = 'Entrando na maior idade'
    
#     if(idade < 18):
#         mensagem = 'Menor de idade'
#     elif(idade > 18):
#         mensagem = 'Maior de idade'
        
#     with open("saida.txt","a",encoding="UTF-8") as arquivo:
#         arquivo.write(f'{nome} {sobrenome} - {mensagem}\n')
    
"""
2 - Faça um programa que leia um arquivo contendo o nome e o prec¸o de diversos produtos
(separados por linha), e calcule o total da compra.
""" 

# with open("produtos.txt","r") as arquivo:
#     dados = arquivo.readlines()
    
#     for ler in dados:
#         print(ler, end='')
  
# soma = 0
# for line in dados:
#     produto, moeda, preco = line.split()
#     soma = float(preco) + soma
# print("-="*30)
# print(f'Total dos produtos: {moeda} {soma:.2f}')

"""
3 - Crie um programa que declare uma estrutura para o cadastro de alunos.
(a) Deverao ser armazenados, para cada aluno: matrıcula, sobrenome (apenas um), e
ano de nascimento.
(b) Ao inıcio do programa, o usuario devera informar o numero de alunos que serao˜
armazenados
(c) O programa devera pedir ao usuario que entre com as informacoes dos alunos. ˜
(d) Em seguida, essas informac¸oes dever ˜ ao ser gravadas em um arquivo ˜
(e) Ao final, mostrar os dados armazenados. 
"""

# quant = int(input('Quantos alunos cadastrar? '))

# for cont in range(quant):
#     print(f'{cont + 1} Aluno(a): ')
#     aluno = input('Nome: ')
#     sobrenome = input('Sobrenome: ')
#     anoDeNascimento = input('Ano de nascimento: ')
#     matricula = input('Matricula: ')
#     print('-='*30)
    
#     with open("cadastro.txt","a") as arquivo:
#         arquivo.write(f'{cont+1} Aluno(a)\nNome: {aluno}\nSobrenome: {sobrenome.split()[0]}\nAno de Nascimento: {anoDeNascimento}\nMatricula: {matricula}\n\n')
        
# print(f'\nNome: {aluno}\nSobrenome: {sobrenome.split()[0]}\nAno de Nascimento: {anoDeNascimento}\nMatricula: {matricula}\n\n')