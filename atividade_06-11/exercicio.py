#ESTRUTURA DE DADOS
#DATA: 06/11/24
#POR JUDAH BENJAMIN

"""
Faça um programa em python para cadastrar clientes e registrar as vendas de floricultura. O programa deverá registrar dados de
clientes(nome,cpf,telefone e email) e os dados das vendas feitas para esses clientes. Cada venda deve conter o nome do cliente, a descrição
do produto (ex.: "Buquê de Rosas", "Orquídea") e o valor total da compra que o cliente fez. Não é necessário implementar controle de 
estoque, quantidades ou informações adicionais dos produtos. O programa deverá permitir ao usuário:
- Cadastrar novos clientes.
- Visualizar a lista de clientes cadastrados.
- Deve permitir registrar vendas somente para clientes já cadastrados.
- Exibir as vendas realizadas por um determinado cliente.
"""

# clientes = []

# def adicionar_clientes():
#     print("============= CADASTRAR CLIENTES ============")
#     lista_clientes = {}

#     print(30*"=-")

#     nome_cliente = input("Digite o nome do cliente: ")
#     cpf_cliente = input("Digite o cpf do cliente: ")
#     telefone_cliente = input("Digite o telefone do cliente: ")
#     email_cliente = input("Digite o email do cliente: ")
    
#     lista_clientes["Cliente:"] = nome_cliente    
#     lista_clientes["CPF:"] = cpf_cliente    
#     lista_clientes["Telefone:"] = telefone_cliente    
#     lista_clientes["E-mail:"] = email_cliente    

#     print(30*"=-")
    
#     clientes.append(lista_clientes)

# def listar_clientes():
#   print()
#   print("Listagem dos clientes inseridos:")
#   for c in clientes:
#       print (c)
      
# def adicionar_venda():
#     print("============= REGISTRAR VENDAS ============")
#     buscar_cliente = input("Digite o cliente que queira buscar: ")
#     for buscar_cliente in clientes:
#         if buscar_cliente in lista_clientes:
#             nome_produto = input("Digite o nome do produto: ")
#             descricao_produto = input("Digite a descrição do produto: ")
#             valor_total = float(input("Digite o valor total da venda: "))
#             produto_vendas = []
#             while True:
#                 produto_vendas.append(nome_produto)
#                 produto_vendas.append(descricao_produto)
#                 produto_vendas.append(valor_total)
#                 nome_produto = input("Digite outro nome do produto (Para terminar digite: 'sair'): ")
#                 if nome_produto == 'sair':
#                     break
#         else:
#             print(f"O cliente {buscar_cliente} não foi encontrado.")

# def exibir_vendas():
#     print()
#     print("Visualização das vendas:")
#     for v in produto_vendas:
#         print (v)


# while True:
#     print("\n--- Menu ---")
#     print("1. Adicionar clientes")
#     print("2. Listar clientes")
#     print("3. Registrar vendas")
#     print("4. Exibir vendas")
#     print("5. Sair")
#     opcao = input("Escolha uma opção: ")
#     print()

#     if opcao =='1':
#         adicionar_clientes()

#     elif opcao == '2':
#         listar_clientes()

#     elif opcao == '3':
#         adicionar_venda()
        
#     elif opcao == '4':
#         exibir_vendas()

#     elif opcao == '5':
#         break
#     else:
#         print("Opção inválida.")