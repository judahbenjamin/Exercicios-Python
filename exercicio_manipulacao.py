#POR JUDAH BENJAMIN - 02/10/24 (ATUALIZADO)
#ESTRUTURA DE DADOS

"""
Crie um programa que deverá controlar os dados de "n" pessoas conforme as características e funcionalidade listadas abaixo:

Registar o nome, telefone, e-mail e cpf e cada pessoa(utilize um dicionário para executar essa operação)
O programa deverá exibir um menu para que o usuário fique informado sobre as operações existentes no programa;
Opção para inserir os dados de uma pessoa
Opção para listar os dados de todas as pessoas
Sair do programa( e gravar os dados que estão contidos na lista de dados)
Atenção: O programa deve carregar os dados contidos no arquivo de "memória" ao ser inicializado. 
"""

import json

pessoas = []

def adicionar_pessoas():
    lista_pessoas = {}
    
    print("======================")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    cpf = input("CPF: ")

    print("======================")

    lista_pessoas["Nome"] = nome
    lista_pessoas["Telefone"] = telefone
    lista_pessoas["Email"] = email
    lista_pessoas["CPF"] = cpf
    
    pessoas.append(lista_pessoas)

def listar_pessoas():
  print()
  print("Listagem das pessoas:")
  for umaPessoa in pessoas:
      print (umaPessoa)

def gravar_dados():
    with open("arquivo.json","w") as arquivo:
        json.dump(pessoas,arquivo)

    with open("arquivo.json","r") as arquivo:
        dados_lidos = json.load(arquivo)
        
while True:
    print("\n--- Menu ---")
    print("1. Adicionar pessoas")
    print("2. Listar pessoas")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    print()

    if opcao =='1':
        adicionar_pessoas()

    elif opcao == '2':
        listar_pessoas()

    elif opcao == '3':
        gravar_dados()
        print("ATENÇÃO! OS DADOS FORAM GRAVADOS")
        print("PROGRAMA FINALIZADO...")
        break
    else:
        print("Opção inválida.")
