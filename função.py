#LÓGICA DE PROGRAMAÇÃO E ALGORITMO
#PROFESSOR: MÁRCIO CLAY
#ALUNO: JUDAH
#DATA: 09/04/2024
#FUNÇÕES EM PYTHON

"""
    As funções ajudam a reduzir a quantidade de linhas em um código,
    facilitam o processo de depuração e permitem criar programas
    mais legíveis e fáceis de manter.

    - Define um bloco de código reutilizável.
    - Estrutura que agrupa partes do código. 
    - As funções cumprem objetivos específicos.
    - Recebem como parâmetro dados de entrada - argumentos.
    - Divide e classifica o código em partes mais simples.
    - Reutiliza o código, evitando repetições.
    
    Tipos de funções em Python:
    
    - Nativas(built - in functions) = opções dispóniveis que já estão integrados
    no Python.
    
    - Personalizadas - criadas pelo usuário.
    
"""


def ImprimirDados ():
    print("Judah Benjamin")
    print("Tecnico em Informatica")

ImprimirDados()

###############################################

def ImprimirNota (media):
    if media >= 7:
        print("APROVADO!")
    else:
        print("REPROVADO!")
    return media

print(ImprimirNota(7))
print(ImprimirNota(10))
print(ImprimirNota(6))
print(ImprimirNota(4))

###############################################

def somar (a, b):
    soma = a + b
    return soma

print(somar(3,4))
print(somar(53,4))
print(somar(30,14))

###############################################

def Concatenar (text1, text2):
    mensagem = f"{text1}{text2}"
    return mensagem

print(Concatenar("Ola, ","Mundo!"))

###############################################

def ImprimirDados (nome, curso):
    mensagem = f"Seu nome e {nome} e seu curso e {curso}"
    return mensagem
    
print(ImprimirDados("Judah","Informatica"))

###############################################

def bem_vindo (nome):
    print("Bem-vindo ao Python, " + nome + "!")
    
bem_vindo("Judah")

###############################################

def Bem_vindo (nome, sobrenome):
    print("Bem-vindo ao Python, " + nome, sobrenome + "!")
    
Bem_vindo("Judah", "Oliveira")
Bem_vindo(nome="Judah", sobrenome="Oliveira")

###############################################

def Impressao(nome,curso):
    print(nome,curso)

nome = input("Digite o nome: ")
curso = input("Digite o curso: ")
Impressao(nome,curso)