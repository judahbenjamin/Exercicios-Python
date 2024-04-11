lista_de_alunos = [] #1 passo - criar um array vazio

def menu(): #2 passo - criar uma funçao menu em que dentro dele varios blocos de código serão executados.
    alunos = ["1 - Incluir","2 - Excluir","3 - Atualizar", "4 - Listar", "5 - Sair"]
    opcao = int(input(f"{alunos}\n Escolha a opcao que deseja: "))
    while opcao != 5: #as condicionais serão executadas dentro do while.
        
        if opcao == 1: #Digitar o nome do aluno e adicionar na lista.
            nome = input("Digite o nome do aluno: ")
            lista_de_alunos.append(nome)
            print(lista_de_alunos)
        elif opcao == 2: #Remover algum nome adiconado dentro da lista.
            nome = input("Digite o nome do aluno que deseja remover: ")        
            lista_de_alunos.remove(nome)
        elif opcao == 3: #Escolher um nome que será alterado em uma posição específica.
            print(lista_de_alunos)
            Alterar_nome = input("Digite o nome que deseja remover: ")
            for c in lista_de_alunos: #o c vai percorrer a lista
                if Alterar_nome == c:
                    posicao = 0
                    nome = input("Qual a alteracao que deseja fazer? ")
                    lista_de_alunos[posicao] = nome
                    break
                else:
                    print("Nome nao encontrado!")
                posicao = posicao + 1
        elif opcao == 4: #mostrar os elementos da lista
            print(f"Listar alunos: {lista_de_alunos}")
        elif opcao == 5:
            print("Programa Finalizado!")
            
        alunos = ["1 - Incluir","2 - Excluir","3 - Atualizar", "4 - Listar", "5 - Sair"]
        opcao = int(input(f"{alunos}\n Escolha a opcao que deseja: "))
menu()