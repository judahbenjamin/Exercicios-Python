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

# def gravaDado_emArquivo(dadoRecebido):
#     with open('arquivo.txt', 'w') as arquivo:
#         arquivo.write("\n"+dadoRecebido)

# def leDados_emArquivo():
#     with open('arquivo.txt', 'r') as arquivo:
#         conteudo = arquivo.read()
#         print(conteudo)

# while True:
#     print("Inserir dados -- 1")
#     print("Exibir dados -- 2")
#     opcao = input("Digite uma opcao: ")

#     if opcao == "1":
#         dadoRecebido = input("Digite um nome: ")
#         gravaDado_emArquivo(dadoRecebido)

#     elif opcao == "2":
#         leDados_emArquivo()


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