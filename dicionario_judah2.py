#ESTRUTURA DE DADOS
#DATA: 10/09/2024
#EXERCÍCIO DICIONÁRIOS 2
#JUDAH BENJAMIN

"""
1. Crie um script em Python e nele adicione um dicionário que deverá receber nome e a
descrição de um objeto. Registre os dados de 10 objetos e após receber todos os dados,
limpe a tela e liste os dados recebidos. Crie uma opção de busca pelo objeto, nela o
usuário deverá informar o nome do objeto e se o objeto for encontrado a descrição
equivalente deverá ser exibido.
"""

# from time import sleep

# listaObjetos = []

# dados_objeto = {
#     "Caderno":{
#         "descricao" : "Objeto composto por folhas de papel agrupadas."
#     },
#     "Estojo":{
#         "descricao": "Caixa com divisões, escaninhos ou repartimentos para guardar algo."
#     },
#     "Mochila":{
#         "descricao": "Um saco de lona ou tecido sintético resistente."
#     },
#     "Apontador":{
#         "descricao": "Objeto cuja função é criar ou manter uma ponta afiada e funcional para um lápis."
#     },
#     "Lapis":{
#         "descricao": "É um instrumento de escrever."
#     },
#     "Caneta":{
#         "descricao": "Instrumento utilizado para aplicar tinta sobre uma superfície."
#     },
#     "Mesa":{
#         "descricao": "Peça de mobiliário feita a partir de diversos materiais."
#     },
#     "Borracha":{
#         "descricao": "Sua principal característica é possuir bastante elasticidade, além de ser um material resiliente."
#     },
#     "Estilete":{
#         "descricao": "Realizar cortes precisos em diferentes superfícies e materiais."
#     },
#     "Apagador":{
#         "descricao": "Remove rapidamente a tinta dos marcadores, garantindo uma superfície livre de resíduos e manchas."
#     }
# }

# listaObjetos.append(dados_objeto)
# sleep(0.4)
# print(f"A lista contem os seguintes objetos: \n{listaObjetos}\n",flush=True)

# nome_objeto = input("Digite o nome do objeto: ")

# if nome_objeto in dados_objeto:
#     sleep(0.4)
#     detalhes = dados_objeto[nome_objeto]
#     print(f"Descricao do objeto: {detalhes["descricao"]}",flush=True)
# else:
#     print(f"O objeto com o nome {nome_objeto} não foi encontrado.")
# sleep(0.4)
# print("PROGRAMA FINALIZADO...")

"""
2. Crie um script em Python onde deverá haver um dicionário que terá como objetivo servir
para armazenar os dados de “n” objetos. O programa deverá permitir ao usuário inserir
os dados de um objeto por vez; listar todos os dados recebidos; permitir ao usuário
buscar os dados de um objeto informando o nome de um objeto, adicionar novas
descrições a um objeto existente. Caso um produto tenha mais de uma descrição o
usuário deverá ter acesso a apenas uma descrição do produto por vez, as descrições
deverão ser exibidas aleatoriamente.(Antes de fazer esta atividade leia com muita
atenção o enunciado)    
"""

# lista_objetos = []
# dados_objetos = {}

# pergunta = input("Deseja iniciar o programa? (S - 1; N - 0) ")

# while (pergunta != 0):
#     objeto = input("Digite o objeto: ")
#     descricao = input("Descreva o objeto: ")
#     lista_objetos.append(objeto)
#     lista_objetos.append(descricao)
    
#     resposta = input("Deseja continuar? (S - 1; N - 0) ")

#     if(resposta != 1):
#         break

# print(f"A lista contem os seguintes objetos: \n{lista_objetos}\n")

# nome_objeto = input("Digite o nome do objeto: ")

# if nome_objeto in dados_objeto:
#     detalhes = dados_objeto[nome_objeto]
#     print(f"Descricao do objeto: {detalhes["descricao"]}",flush=True)
# else:
#     print(f"O objeto com o nome {nome_objeto} não foi encontrado.")

# print("PROGRAMA FINALIZADO...")

objetos = {}

while True:
    nome_objeto = input("Nome do objeto: ")
    descricao_objeto = input("Descrição do objeto: ")

    objetos[nome_objeto] = descricao_objeto

    opcao = int(input("DESEJA CONTINUAR? ( S - 1 ; N - 0 ) "))

    if opcao == 0:
        break
print()
print(f"Listando os objetos: \n{objetos}")

nome_objeto = input("Digite o nome do objeto: ")

if nome_objeto in objetos:
    digitar = int(input("Deseja digitar uma descricao extra? (S - 1; N - 0) "))

    if digitar == 0:
        detalhes2 = objetos[nome_objeto]
        print(f"Descricao do objeto: {detalhes2}")
    elif digitar == 1:
        detalhes3 = input("Digite uma outra descricao: ")
        detalhes1 = objetos[nome_objeto]
        detalhes2 = objetos[nome_objeto]
        print(f"Descricao do objeto: {detalhes2}")
        print(f"Outra descricao do mesmo objeto: {detalhes3}")
        objetos[nome_objeto] = descricao_objeto
        print(objetos)
else:
    print("DEU ERRO.")

print("FIM DO PROGRAMA...")
