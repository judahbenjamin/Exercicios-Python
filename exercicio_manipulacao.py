#POR JUDAH BENJAMIN - 25/09/24
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

# dados_pessoa = []

# def gravando_em_arquivo(nome,telefone,email,cpf):
#     with open('arquivo.txt','w') as arquivo:
#         arquivo.write("\n"+nome)
#         arquivo.write("\n"+telefone)
#         arquivo.write("\n"+email)
#         arquivo.write("\n"+cpf)

# def ler_arquivos():
#     with open('arquivo.txt','r') as arquivo:
#         conteudo = arquivo.read()
#         return conteudo
    
# dado_programa = ler_arquivos()

# while True:

#     print("========= MENU =========")
#     print("Insere dados --------- 1")
#     print("Exibe dados ---------- 2")
#     print("Sair do programa ----- 3")
#     opcao = int(input("Digite uma opcao: "))

#     if opcao == 1:
#         dados_pessoa = {}
#         nome = input("Nome da pessoa: ")
#         telefone = input("Telefone da pessoa: ")
#         email = input("E-mail da pessoa: ")
#         cpf = input("CPF da pessoa: ")
#         print()
#         gravando_em_arquivo(nome,telefone,email,cpf)

#     elif opcao == 2:
#         print(ler_arquivos())
#         print()

#     elif opcao == 3:
#         print("PROGRAMA FINALIZADO...")
#         break

import json

# Dicionário de exemplo

cont = 0
quant = int(input("Digite quantidade de vezes? "))

for cont in range(cont):

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")

    pessoa = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade
    }

#PROCESSO DE GRAVAÇÃO DE DICIONÁRIO EM ARQUIVO.
#
# Grava o dicionário em um arquivo chamado 'dicionario.json'
with open('arquivo.txt', 'w') as arquivo:
    json.dump(pessoa, arquivo)
    #Faz a união do dicionário com o objeto arquivo.


#PROCESSO DE LEITURA EM ARQUIVO DE UM DICIONÁRIO.
#
# Inicializa um dicionário vazio para guardar os dados recebidos.
dadosRecebidos = {}

# Abre o arquivo 'dicionario.json' para leitura
with open('arquivo.txt', 'r') as arquivo:
    # Carrega os dados do arquivo para o dicionario_lido
    dicionario_lido = json.load(arquivo)

# Exibe o dicionário lido do arquivo
print(dicionario_lido)
