#LÓGICA DE PROGRAMAÇÃO E ALGORITMO
#PROFESSOR: MÁRCIO CLAY
#ALUNO: JUDAH
#DATA: 10/04/2024
#EXERCICIO


print("====================== CADASTRO DE ALUNOS =====================")

alunos = []

def menu():
    menu_opcao = ["1 - Incluir"," 2 - Excluir","3 - Atualizar","4 - Listar","5 - Sair"]
    opcao = int(input(f"{menu_opcao}\n Digite a opcao: "))
    while opcao != 5:

        if opcao == 1:
            nome = input("Digite um nome:")
            alunos.append(nome)
            print(alunos)
        elif opcao == 2:
            nome = input("Digite o nome que deseje remover: ")
            alunos.remove(nome)   
        elif opcao == 3:
            print(alunos)
            alterar_nome = input("Digite o nome que você quer alterar: ")
            for c in alunos:
                if alterar_nome == c:
                    posicao = 0
                    nome = input("Digite a posicao que deseje alterar: ")
                    alunos[posicao] = nome
                    break
                else:
                    print("Nome nao encontrado!")
                posicao = posicao + 1
        elif opcao == 4:
            print(f"A lista: {alunos}")
            
        menu_opcao = ["1 - Incluir"," 2 - Excluir","3 - Atualizar","4 - Listar","5 - Sair"]
        opcao = int(input(f"{menu_opcao}\n Digite a opcao: "))          
menu()
        
