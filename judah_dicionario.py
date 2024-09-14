#ALGORITMOS E LÓGICA DE PROGRAMAÇÃO
#DATA: 06/09/24
#JUDAH BENJAMIN
#EXERCICIOS DE DICIONÁRIOS

"""
1 - Crie um script e nele adicione um dicionário que deverá receber nome e o telefone de 10 pessoas. Após
receber todos os dados, liste os dados recebidos. Crie uma opção de busca pelo nome, se o nome for encontrado
o telefone será exibido.
"""

# from time import sleep

# listaPessoas = []

# dados_pessoas = {
#     "Alfredo":{
#         "telefone" : "9999-9999"
#     },
#     "Joao Pedro":{
#         "telefone": "2222-2222"
#     },
#     "Pedro Silva":{
#         "telefone": "1111-1111"
#     },
#     "Lucas":{
#         "telefone": "1212-1212"
#     },
#     "Ana Maria":{
#         "telefone": "3232-3232"
#     },
#     "Juliana":{
#         "telefone": "8989-9898"
#     },
#     "Leticia Santos":{
#         "telefone": "7890-0987"
#     },
#     "Eduarda Fernandes":{
#         "telefone": "4500-7800"
#     },
#     "Daniel Soares":{
#         "telefone": "1245-9876"
#     },
#     "Jaqueline Matos":{
#         "telefone": "3456-0976"
#     }
# }

# listaPessoas.append(dados_pessoas)
# sleep(0.4)
# print(f"A lista contem as seguintes pessoas: \n{listaPessoas}\n",flush=True)

# nome = input("Digite o nome: ")

# if nome in dados_pessoas:
#     sleep(0.4)
#     detalhes = dados_pessoas[nome]
#     print(f"Telefone: {detalhes["telefone"]}",flush=True)
# else:
#     print(f"A pessoa com o nome {nome} não foi encontrada.")
# sleep(0.4)
# print("PROGRAMA FINALIZADO...")

"""
2 -  Crie um script e nele adicione um dicionário que deverá receber nome do
cliente de uma oficina de veículos, neste programa deverão ser registrados a
placa do veículo, a cor do veículo, marca do veículo e a data de entrada do
veículo na oficina. O programa deverá ser capaz de fazer o registro dos
veículos, fazer a listagem dos veículos e fazer a busca de um determinado
veículo tendo como critério de busca a placa do veículo. 
"""

# oficina_veiculos = []

# lista_veiculos = {
#     "LSW3445":{
#         "Cliente" : "Paulo Neves",
#         "Carro" : "Sienna",
#         "Placa" : "LSW3445",
#         "Cor" : "Vermelho",
#         "Marca" : "Fiat",
#         "Data_entrada" : "24/09/2010"
#     },
#     "BRAZ2379":{
#         "Cliente" : "Carlos Silva",
#         "Carro" : "Gol",
#         "Placa" : "BRAZ2379",
#         "Cor" : "Cinza",
#         "Marca" : "Volkswagen",
#         "Data_entrada" : "01/07/2008"
#     },
#     "T5RR2020":{
#         "Cliente" : "Joana Maria",
#         "Carro" : "Uno",
#         "Placa" : "T5RR2020",
#         "Cor" : "Amarelo",
#         "Marca" : "Fiat",
#         "Data_entrada" : "20/01/2007"
#     },
#     "ZT452334":{
#         "Cliente" : "Luiza Alves",
#         "Carro" : "Jipe",
#         "Placa" : "ZT452334",
#         "Cor" : "Branco",
#         "Marca" : "Jeep",
#         "Data_entrada" : "10/02/2007"
#     }
    
# }

# oficina_veiculos.append(lista_veiculos)
# print(f"Lista dos clientes da oficina de veiculos:\n{oficina_veiculos}")
# print()
# placa = input("Digite a placa: ")
# print()
# if placa in lista_veiculos:
#     busca = lista_veiculos[placa]
#     print(f"Cliente: {busca["Cliente"]}")
#     print(f"Carro: {busca["Carro"]}")
#     print(f"Placa: {busca["Placa"]}")
#     print(f"Cor: {busca["Cor"]}")
#     print(f"Marca: {busca["Marca"]}")
#     print(f"Data de entrada: {busca["Data_entrada"]}")
# else:
#     print(f"Veículo com a placa {placa} não encontrado.")
# print("PROGRAMA ENCERRADO...")

"""
3 - Crie um script e nele adicione um dicionário que deverá receber nome e notas
de 5 alunos, cada aluno deve receber 4 notas. Após receber todos os dados,
liste separadamente os dados dos alunos aprovados e reprovados. Um aluno
é aprovado com a somatória das notas >= a 60 pontos, apresente também a
somatória das notas de cada aluno.   
"""

# aprovados = []
# reprovados = []

# Alunos = {}

# Alunos["Pedro"] = [10.0, 19.0, 19.5, 20]
# Alunos["Ana"] = [8.5, 9.0, 10.0, 10.0]
# Alunos["Maria"] = [37.5, 10.0, 26.6, 5.0]
# Alunos["Joao"] = [29.0, 14.5, 13.0, 10.0]
# Alunos["Juliana"] = [10.0, 10.0, 10.0, 9.5]
  
# print("===== Nota dos Alunos =====")
# for soma in Alunos:
#     alunos = Alunos[soma]
#     print(f"Nome do aluno: {soma}. Nota: {sum(alunos)}")
#     if sum(alunos) >= 60:
#         aprovados.append(soma)
#     else:
#         reprovados.append(soma)
       
# print()
# print("===== Media dos Alunos =====")
# for media in Alunos:
#     alunos = Alunos[media]
#     print(f"Media do aluno {media} : {(sum(alunos)/len(alunos)):.2f}")

# print()
# print("============ RESULTADO ============") 
# print(f'Os aprovados foram: {aprovados}')
# print(f'Os reprovados foram: {reprovados}')

"""
4 - Crie um script e nele adicione um dicionário que deverá receber nome e notas
de “n” alunos, cada aluno deve receber 4 notas. O programa criado deverá
apresentar as seguintes características/funcionalidades:
a. Receber os dados de um aluno por vez;
b. Exibir os dados dos alunos de uma só vez(indicando a somatória das notas de
cada aluno);
c. Exibir a lista dos alunos aprovados e reprovados(só os nomes e a indicação de
aprovado e reprovado - se possível duas opções, uma para aprovados e outra
para reprovados);
d. Exibir um menu com as opções existentes no programa.    
"""

# Alunos = {}
# nomes = []
# alunos_notas = []

# quant = int(input("Informe a quantidade de alunos: "))
# cont = 0

# while(cont < quant):
#     nome_aluno = input("Nome: ")
#     n1 = float(input("Nota 1: "))
#     n2 = float(input("Nota 2: "))
#     n3 = float(input("Nota 3: "))
#     n4 = float(input("Nota 4: "))

#     notas = n1,n2,n3,n4
#     soma_notas = sum(notas)

#     print(f"Nome do aluno: {nome_aluno}\nNota: {(soma_notas)}")
#     alunos_notas.append(nome_aluno)
#     alunos_notas.append(soma_notas)
#     nomes.append(alunos_notas)
#     print(nomes)  

#CÓDIGO CORRIGIDO

# def criar_aluno():
#     nome = input("Digite o nome do aluno: ")
#     notas = []
#     for i in range(4):
#         nota = float(input(f"Digite a {i+1}ª nota: "))
#         notas.append(nota)
#     return nome, notas

# def calcular_media(notas):
#     return sum(notas) / len(notas)

# def aprovado_reprovado(media):
#     return "Aprovado" if media >= 7 else "Reprovado"

# def exibir_alunos(alunos):
#     for aluno, notas in alunos.items():
#         media = calcular_media(notas)
#         print(f"Aluno: {aluno}")
#         print(f"Notas: {notas}")
#         print(f"Média: {media:.2f} - {aprovado_reprovado(media)}")
#         print("-" * 20)

# def exibir_aprovados_reprovados(alunos):
#     aprovados = []
#     reprovados = []
#     for aluno, notas in alunos.items():
#         media = calcular_media(notas)
#         if media >= 7:
#             aprovados.append(aluno)
#         else:
#             reprovados.append(aluno)

#     print("Alunos Aprovados:")
#     for aluno in aprovados:
#         print(aluno)

#     print("\nAlunos Reprovados:")
#     for aluno in reprovados:
#         print(aluno)

# def main():
#     alunos = {}
#     while True:
#         print("\n--- Menu ---")
#         print("1. Cadastrar novo aluno")
#         print("2. Exibir todos os alunos")
#         print("3. Exibir aprovados e reprovados")
#         print("4. Sair")
#         opcao = int(input("Escolha uma opção: "))

#         if opcao == 1:
#             nome, notas = criar_aluno()
#             alunos[nome] = notas
#         elif opcao == 2:
#             exibir_alunos(alunos)
#         elif opcao == 3:
#             exibir_aprovados_reprovados(alunos)
#         elif opcao == 4:
#             break
#         else:
#             print("Opção inválida.")

# if __name__ == "__main__":
#     main()
