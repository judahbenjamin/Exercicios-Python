ListaGeralPessoas = []

while True:
    print()
    print("####             MENU            ####")
    print("Inserir Dados Pessoa            < 1 >")
    print("Listar Pessoas                  < 2 >")
    print("Sair                            < 9 >")
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

        ListaGeralPessoas.append(listaDadoPessoa)

    if opcao == "2":
        print("\n\n#### Lista dos dados inseridos   ###")
        for dadosUmaPessoa in ListaGeralPessoas:
            nome, telefone, cpf, salario = dadosUmaPessoa

    if opcao == "9":
        print("PROGRAMA ENCERRADO...")
        break
