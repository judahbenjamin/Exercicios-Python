lista_alunos = []

def menu():
    print("1 - Incluir, 2 - Excluir, 3 - Atualizar, 4 - Listar, 5 - Sair")
    opcao = 0

    while opcao != 5:
        
        opcao = int(input("Digite a opcao que deseja: "))
    
        if opcao == 1:
            Incluir()
        elif opcao == 2:
            Excluir()
        elif opcao == 3:
            Atualizar()
        elif opcao == 4:
            Listar()
        elif opcao == 5:
            Sair()
        
        
def Incluir():
    nome = input("Digite o nome do aluno: ")
    lista_alunos.append(nome)
    print(lista_alunos)
    
def Excluir():
    nome = input("Digite o nome que deseje remover: ")
    lista_alunos.remove(nome)

def Atualizar():
    print(lista_alunos)
    alterar_nome = input("Digite o nome pra remover: ")
    for x in lista_alunos:
        if alterar_nome == x:
            posicao = int(input("Digite a posicao desse nome: "))
            nome = input("Qual a alteracao que deseja fazer?")
            lista_alunos[posicao] = nome
            break
       
        
def Listar():
    print(f"A lista: {lista_alunos}")

def Sair():
    print("Programa finalizado!")
    
menu()  