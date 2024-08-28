#ESTRUTURA DE DADOS 
#JUDAH BENJAMIN
#DATA: 28/08/2024

ListaGeralPessoas = []

while True:
    print()
    print("####             MENU            ####")
    print("Inserir Dados Pessoa            < 1 >")
    print("Listar Pessoas                  < 2 >")
    print("Visualizacao resumida           < 3 >")
    print("Busca do funcionario            < 4 >")
    print("Sair                            < 5 >")
    opcao = input("Digite a opcao: ")

    if opcao == "1":

        listaDadoPessoa = []

        print("\n\n#####    Inserir dados Pessoa    #####")
        nome = input("Digite nome: ")
        listaDadoPessoa.append(nome)

        telefone = input("Digite telefone: ")
        listaDadoPessoa.append(telefone)

        cpf = input("Digite CPF: ")
        listaDadoPessoa.append(cpf)

        rg = input("Digite RG: ")
        listaDadoPessoa.append(rg)

        email = input("Digite E-mail: ")
        listaDadoPessoa.append(email)

        salario = float(input("Informe salário: "))
        listaDadoPessoa.append(salario)

        quant_filhos = int(input("Digite quantidade de filhos: "))
        listaDadoPessoa.append(quant_filhos)

        ListaGeralPessoas.append(listaDadoPessoa)

    if opcao == "2":
        print("\n\n#### Lista dos dados inseridos   ###")
        for dadosUmaPessoa in ListaGeralPessoas:
            nome, telefone, cpf, rg, email, salario, quant_filhos = dadosUmaPessoa
            print(f"Nome : {nome} - Telefone: {telefone} - CPF: {cpf} - RG: {rg} - E-mail: {email} - Salário: {salario} - Quantidade de filhos: {quant_filhos}")


    if opcao == "3":
        print("\n\n#### Visualizacao resumida   ###")
        for dadosUmaPessoa in ListaGeralPessoas:
            nome, telefone, cpf, rg, email, salario, quant_filhos = dadosUmaPessoa
            print(f"Nome: {nome} - CPF: {cpf}")

    if opcao == "4":
        print("\n\n#### Busca do funcionario   ###")

        busca_funcionario = input("Digite o funcionario: ")
        b = 0

        for dadosUmaPessoa in ListaGeralPessoas:
            nome, telefone, cpf, rg, email, salario, quant_filhos = dadosUmaPessoa

            if busca_funcionario == nome:
                print(f"Nome : {nome} - Telefone: {telefone} - CPF: {cpf} - RG: {rg} - E-mail: {email} - Salário: {salario} - Quantidade de filhos: {quant_filhos}")
                b = 1

            if busca_funcionario == 0:
                print("\nInvalido")

    if opcao == "5":
        print("PROGRAMA ENCERRADO...")
        break