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

dados_pessoa = []

def gravando_em_arquivo(nome,telefone,email,cpf):
    with open('arquivo.txt','w') as arquivo:
        arquivo.write("\n"+nome)
        arquivo.write("\n"+telefone)
        arquivo.write("\n"+email)
        arquivo.write("\n"+cpf)

def ler_arquivos():
    with open('arquivo.txt','r') as arquivo:
        conteudo = arquivo.read()
        return conteudo
    
dado_programa = ler_arquivos()

while True:

    print("========= MENU =========")
    print("Insere dados --------- 1")
    print("Exibe dados ---------- 2")
    print("Sair do programa ----- 3")
    opcao = int(input("Digite uma opcao: "))

    if opcao == 1:
        dados_pessoa = {}
        nome = input("Nome da pessoa: ")
        telefone = input("Telefone da pessoa: ")
        email = input("E-mail da pessoa: ")
        cpf = input("CPF da pessoa: ")
        print()
        gravando_em_arquivo(nome,telefone,email,cpf)

    elif opcao == 2:
        print(ler_arquivos())
        print()

    elif opcao == 3:
        print("PROGRAMA FINALIZADO...")
        break