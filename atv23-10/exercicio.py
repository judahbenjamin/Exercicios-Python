#ESTRUTURA DE DADOS
#POR JUDAH BENJAMIN - 23/10/24

"""
Crie um programa que deverá armazenar termos e suas respectivas descrições, o referido programa deverá apresentar as seguintes característias/ funcionalidades:

Apresentar uma opção para o usuário indicar a inserção do termo e sua descrição;
Um termo pode ter uma ou mais descrições;
Apresentar uma opção para a operação de busca de um termo, se o termo for localizado o programa deve exibir todas as descrições referentes a equele termo.

Atenção:
As buscas devem localizar os dados idênticos e similares(grafia próxima da original), defina o nível de coeficiente a ser aceito.
Não usar biblioteca/classes prontas do Python para resolver essa situação.
Cuidado com o uso de IA's
O uso de códigos "Similares" provocará com que a atividade seja ignorada. 
"""

# termos = []

# def adicionar_termos():
#     lista_termos = {}
    
#     print(30*"=-")

#     nome_termo = input("Digite o nome do termo: ")
#     descricao_termo = input("Digite a descrição do termo: ")
#     descricoes_termos = []
#     while descricao_termo != 'sair':
#         descricoes_termos.append(descricao_termo)
#         descricao_termo = input("Digite outra descrição do termo (Para terminar digite: 'sair'): ")
#     lista_termos["Descrições"] = descricoes_termos    

#     print(30*"=-")

#     lista_termos["Termo"] = nome_termo
    
#     termos.append(lista_termos)

# def listar_termos():
#   print()
#   print("Listagem dos termos inseridos:")
#   for t in termos:
#       print (t)
      
# def buscar_termos():
#     buscar_termo = input("Digite o termo que queira buscar: ")
#     if buscar_termo in listar_termos:
#         print("Descrições:")
#         for descricao in listar_termos[buscar_termo]:
#             print(f"{descricao}")
#     else:
#         print(f"O termo {buscar_termo} não foi encontrado.")

# while True:
#     print("\n--- Menu ---")
#     print("1. Adicionar termos")
#     print("2. Listar termos")
#     print("3. Buscar termos")
#     print("4. Sair")
#     opcao = input("Escolha uma opção: ")
#     print()

#     if opcao =='1':
#         adicionar_termos()

#     elif opcao == '2':
#         listar_termos()

#     elif opcao == '3':
#         buscar_termos()
        
#     elif opcao == '4':
#         break
#     else:
#         print("Opção inválida.")


