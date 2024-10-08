# ESTRUTURA DE DADOS
#POR JUDAH BENJAMIN - 02/10/24

"""
1. Crie um script em Python que deverá permitir ao usuário cadastrar dados de
"n" pessoas (nome). O programa deverá apresentar um menu com as
seguintes opções:
    a. Inserir os dados de uma pessoa (um registro por vez);
    b. Listar todos os dados das pessoas cadastradas;
    c. Finalizar o programa.
    d. Ao ser finalizado, o programa deverá salvar os dados cadastrados em um
    arquivo. Quando o programa for iniciado, ele deverá carregar os dados do
    arquivo para continuar o cadastro.
"""

# import json

# nomes = []

# def adicionar_nomes():
#     lista_nomes = {}
    
#     print(30*"=-")

#     nome = input("Digite um nome: ")

#     print(30*"=-")

#     lista_nomes["Nome"] = nome
    
#     nomes.append(lista_nomes)

# def listar_nomes():
#   print()
#   print("Listagem dos nomes cadastrados:")
#   for umNome in nomes:
#       print (umNome)

# def gravar_dados():
#     with open("arquivo1.json","w") as arquivo:
#         json.dump(nomes,arquivo)

#     with open("arquivo1.json","r") as arquivo:
#         dados_lidos = json.load(arquivo)
        
# while True:
#     print("\n--- Menu ---")
#     print("1. Adicionar nomes")
#     print("2. Listar nomes")
#     print("3. Sair")
#     opcao = input("Escolha uma opção: ")
#     print()

#     if opcao =='1':
#         adicionar_nomes()

#     elif opcao == '2':
#         listar_nomes()

#     elif opcao == '3':
#         gravar_dados()
#         print("ATENÇÃO! OS DADOS FORAM GRAVADOS")
#         print("PROGRAMA FINALIZADO...")
#         break
#     else:
#         print("Opção inválida.")


"""
2. Crie um script em Python que permita cadastrar dados de "n" pessoas (nome,
CPF, RG, e-mail). O programa deverá apresentar um menu com as seguintes
opções:
    a. Inserir os dados de uma pessoa (um registro por vez);
    b. Listar todos os dados das pessoas cadastradas;
    c. Finalizar o programa.
    d. Ao ser finalizado o programa deverá salvar os dados cadastrados em um
    arquivo e, ao ser inicializado novamente, o programa deverá carregar os
    dados do arquivo para continuar o cadastro.
"""

# import json

# dados_pessoas = []

# def adicionar_pessoas():
#     lista_pessoas = {}
    
#     print(30*"=-")

#     nome = input("Digite o nome: ")
#     cpf = input("Digite o cpf: ")
#     rg = input("Digite o rg: ")
#     email = input("Digite o e-mail: ")

#     print(30*"=-")

#     lista_pessoas["Nome"] = nome
#     lista_pessoas["CPF"] = cpf
#     lista_pessoas["RG"] = rg
#     lista_pessoas["E-mail"] = email
    
#     dados_pessoas.append(lista_pessoas)

# def listar_dados():
#   print()
#   print("Listagem das pessoas cadastradas:")
#   for dado in dados_pessoas:
#       print (dado)

# def gravar_dados():
#     with open("arquivo2.json","w") as arquivo:
#         json.dump(dados_pessoas,arquivo)

#     with open("arquivo2.json","r") as arquivo:
#         dados_lidos = json.load(arquivo)
        
# while True:
#     print("\n--- Menu ---")
#     print("1. Adicionar pessoas")
#     print("2. Listar pessoas")
#     print("3. Sair")
#     opcao = input("Escolha uma opção: ")
#     print()

#     if opcao =='1':
#         adicionar_pessoas()

#     elif opcao == '2':
#         listar_dados()

#     elif opcao == '3':
#         gravar_dados()
#         print("ATENÇÃO! OS DADOS FORAM GRAVADOS")
#         print("PROGRAMA FINALIZADO...")
#         break
#     else:
#         print("Opção inválida.")


"""
3. Crie um script em Python que deverá permitir ao usuário cadastrar os dados
de "n" pessoas (nome, CPF, RG, e-mail, endereço). O programa deverá
apresentar as seguintes características/ funcionalidades:
    a. Apresentar um menu;
    b. Inserir os dados de uma pessoa (um registro por vez);
    c. O usuário poderá buscar os dados de uma pessoa utilizando o cpf como critério de busca;
    d. Listar todos os dados cadastrados;
    e. Ao ser finalizado o programa deverá salvar os dados cadastrados em um
    arquivo e, ao ser inicializado novamente, o programa deverá carregar os
    dados do arquivo para continuar o cadastro.
"""

# import json

# dados_pessoas = []
# dados_pessoas2 = []

# def adicionar_pessoas():
#     lista_pessoas = {}
    
#     print(30*"=-")

#     nome = input("Digite o nome: ")
#     cpf = input("Digite o cpf: ")
#     rg = input("Digite o rg: ")
#     email = input("Digite o e-mail: ")
#     endereco = input("Digite o endereco: ")

#     print(30*"=-")

#     lista_pessoas["Nome"] = nome
#     lista_pessoas["CPF"] = cpf
#     lista_pessoas["RG"] = rg
#     lista_pessoas["E-mail"] = email
#     lista_pessoas["Endereco"] = endereco
    
#     dados_pessoas.append(lista_pessoas)

# def listar_dados():
#   print()
#   print("Listagem das pessoas cadastradas:")
#   for dado in dados_pessoas:
#       print (dado)

# # def buscar_dados():
# #         b = input("Digite o CPF da pessoa: ")

# #         #fazer um for aninhado
# #         for b in dados_pessoas:
# #             for b in dados_pessoas:
# #                 detalhes = dados_pessoas[b]
# #                 print(f"Nome: {detalhes["Nome"]}")
# #                 print(f"CPF: {detalhes["CPF"]}")
# #                 print(f"RG: {detalhes["RG"]}")
# #                 print(f"E-mail: {detalhes["E-mail"]}")
# #                 print(f"Endereco: {detalhes["Endereco"]}")
# #         else:
# #             print(f"A pessoa com o nome {b} não foi encontrada.")
        
# def listar_dados():
#   print()
#   print("Listagem das pessoas cadastradas:")
#   for dado in dados_pessoas:
#       print (dado)


# # ler dados do arquivo dados1.txt e gravar estes dados na lista dados_pessoas
# def gravar_dados():
#     with open("arquivo1.json","w") as arquivo:
#         json.dump(dados_pessoas,arquivo)

#     with open("arquivo1.json","r") as arquivo:
#         dados_pessoas2 = arquivo.readline(dados_pessoas)
#         print(dados_pessoas2)
    
# while True:
#     print("\n--- Menu ---")
#     print("1. Adicionar pessoas")
#     print("2. Buscar dados")
#     print("3. Listar pessoas")
#     print("4. Sair")
#     opcao = input("Escolha uma opção: ")
#     print()

#     if opcao =='1':
#         adicionar_pessoas()

#     elif opcao == '2':
#         buscar_dados()

#     elif opcao == '3':
#         listar_dados()

#     elif opcao == '4':
#         gravar_dados()
#         print("ATENÇÃO! OS DADOS FORAM GRAVADOS")
#         print("PROGRAMA FINALIZADO...")

#         #acionar função para gravar dados da lista em um arquivo de texto, exp: dados1.txt

#         break
#     else:
#         print("Opção inválida.")


"""
4. Crie um script em Python que deverá permitir ao usuário cadastrar os dados
de "n" pessoas (nome, CPF, RG, e-mail, endereço e diversos telefones). O
programa deverá apresentar as seguintes características/funcionalidades:
    a. Apresentar um menu;
    b. Inserir os dados de uma pessoa (um registro por vez);
    c. O usuário poderá buscar os dados de uma pessoa utilizando o nome como critério de busca;
    d. O usuário poderá buscar os dados de uma pessoa utilizando o CPF como critério de busca;
    e. Listar todos os dados cadastrados;
    f. Excluir um registro utilizando o CPF como critério;
    g. Ao ser finalizado, o programa deverá salvar os dados cadastrados em um
    arquivo e, ao ser inicializado novamente, deverá carregar os dados do
    arquivo para continuar o cadastro.
"""

# import json

# dados_pessoas = []

# def adicionar_pessoas():
#     lista_pessoas = {}
    
#     print(30*"=-")

#     nome = input("Digite o nome: ")
#     cpf = input("Digite o cpf: ")
#     rg = input("Digite o rg: ")
#     email = input("Digite o e-mail: ")
#     endereco = input("Digite o endereco: ")
#     telefone = input("Digite o telefone: ")

#     print(30*"=-")

#     lista_pessoas["Nome"] = nome
#     lista_pessoas["CPF"] = cpf
#     lista_pessoas["RG"] = rg
#     lista_pessoas["E-mail"] = email
#     lista_pessoas["Endereco"] = endereco
#     lista_pessoas["Telefone"] = telefone

    
#     dados_pessoas.append(lista_pessoas)

# def listar_dados():
#   print()
#   print("Listagem das pessoas cadastradas:")
#   for dado in dados_pessoas:
#       print (dado)

# def buscar_dados():
#         busca = input("Digite a busca (1 - CPF; 2 - Telefone): ")

#         if busca == '1':
#             print("Ok")
#             # if cpf in dados_pessoas:
#             #     detalhes = dados_pessoas[cpf]
#             #     print(f"Nome: {detalhes["Nome"]}")
#             #     print(f"CPF: {detalhes["CPF"]}")
#             #     print(f"RG: {detalhes["RG"]}")
#             #     print(f"E-mail: {detalhes["E-mail"]}")
#             #     print(f"Endereco: {detalhes["Endereco"]}")
#             # else:
#             #     print(f"A pessoa com o nome {cpf} não foi encontrada.")
#         elif busca == '2':
#             print("Ok dnv")


# def listar_dados():
#   print()
#   print("Listagem das pessoas cadastradas:")
#   for dado in dados_pessoas:
#       print (dado)
    
# while True:
#     print("\n--- Menu ---")
#     print("1. Adicionar pessoas")
#     print("2. Buscar dados")
#     print("3. Listar pessoas")
#     print("4. Sair")
#     opcao = input("Escolha uma opção: ")
#     print()

#     if opcao =='1':
#         adicionar_pessoas()

#     elif opcao == '2':
#         buscar_dados()

#     elif opcao == '3':
#         listar_dados()

#     elif opcao == '4':
#         print("ATENÇÃO! OS DADOS FORAM GRAVADOS")
#         print("PROGRAMA FINALIZADO...")
#         break
#     else:
#         print("Opção inválida.")
