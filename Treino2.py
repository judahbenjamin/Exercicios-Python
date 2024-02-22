# Aluno: Judah Benjamin
#Treino 
# Data: 22/02/2024

"""
x = 5
y = "Texto"
z = 3.0
a = True
b = False

print(x, y, z, a, b)

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))

MyVariable = 1
myVariable = "Olá"
my_variable = True

t = 'Hello'
j = 'World'

#########################################################################

Idade = 12
IDADE = 23
idade = 40

##########################################################################

x = str("Hello World")
x = int(20)
print(x)

"""

#EXERCICIOS

"""
1 - João tem 3 carros e Maria tem 5 carros. Eles foram brimncar com
Pedro no quintal. E José levou seus 8 carros. Quantos carros estavam
no quintal?
"""

Joao = 3
Maria = 5
Jose = 8
Soma = Joao + Maria + Jose
print("A soma dos carros e:", Soma)

"""
2 - Multiplique os seguintes números 20 e 3500, e imprime na tela.
"""

N1 = 20
N2 = 3500
Multiplica = N1 * N2
print("O Valor dos dois numeros sera:",Multiplica)

"""
3 - Calcule a Média de uma alno e obtenha as suas 2 notas de provas.
Se a média for maior ou igual a 7, o aluno foi aprovado. Se não, reprovado.
"""

#Nota1 = float(input("Digite sua primeira nota:"))
#Nota2 = float(input("Digite sua segunda nota:"))

##if Media >=7 :
    #print("Parabéns, você está aprovado.")
#else :
    #print("Sinto muito, mas você está reprovado.")
    
#print("FIM")

"""
4 - Faça um programa que digite um nome. Após isso,
faça-o imprimir na tela.
"""

#nome = input("Digite o seu nome:")
#print("Seja bem vindo,",nome)

"""
5 - Faça a soma de X = 10 e y = 35, e também a multiplicação
destes, e imprima na tela os resultados de X e Y.
"""

X = 10
Y = 35
SOMA = X + Y
MULTIPLICACAO = X * Y

print("A soma de X e Y e:", SOMA)
print("A multiplicacao de X e Y e:",MULTIPLICACAO)

"""
6 - Faça um programa que digite idade. Se a sua idade for maior
que 18, você já é um adulto. Se não, você é adolescente. 
"""

"""Idade = int(input("Digite a sua idade:"))
    
if Idade >= 18 :
     print("Você já é um ADULTO")
else :
     print("Você é um ADOLESCENTE")"""
     
"""
7 - Faça um questionário sobre o cadastro do usuário. Se o usuário
for cadastrado no sistema, peça-o para fazer o login digitando o seu
email e senha. Se nao, peça os seguintes dados pessoais: Nome Completo,
Data de Nascimento, Naturalidade, Email e criar senha.
"""

cadastro = int(input("Voce esta cadastrado no Gov?Se sim digite 1, senao 0:"))

if cadastro == 1:
    email = input("Digite o seu E-mail:")
    senha = input("Digite sua senha:")
    print(email)
    print(senha)
    print("Logado com sucesso!")
else :
    Nome = input("Digite o seu nome completo:")
    DataNasc = input("Informe sua data de nascimento:")
    Naturalidade = input("Digite sua naturalidade:")
    Email = input("Digite se E-mail:")
    Senha = input("Por fim, informe a sua senha:")
    print("Confere seus dados:")
    print(Nome)
    print(DataNasc)
    print(Naturalidade)
    print(Email)
    print(Senha)
    
    correto = int(input("Os dados estão corretos? Se sim, digite um numero maior que 0. Se nao digite menor que 0:"))
    
    if correto > 0 :
        print("CADASTRO concluido.")
    else :
        print("Tente Novamente!")
    
    print("FIM")
