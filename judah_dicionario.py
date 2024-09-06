#ALGORITMOS E LÓGICA DE PROGRAMAÇÃO
#DATA: 06/09/24
#JUDAH BENJAMIN
#EXERCICIOS DE DICIONÁRIOS

# 1. Crie um script e nele adicione um dicionário que deverá receber nome e o telefone de 10 pessoas. Após
# receber todos os dados, liste os dados recebidos. Crie uma opção de busca pelo nome, se o nome for encontrado
# o telefone será exibido.

from time import sleep

listaPessoas = []

dados_pessoas = {
    "Alfredo":{
        "telefone" : "9999-9999"
    },
    "Joao Pedro":{
        "telefone": "2222-2222"
    },
    "Pedro Silva":{
        "telefone": "1111-1111"
    },
    "Lucas":{
        "telefone": "1212-1212"
    },
    "Ana Maria":{
        "telefone": "3232-3232"
    },
    "Juliana":{
        "telefone": "8989-9898"
    },
    "Leticia Santos":{
        "telefone": "7890-0987"
    },
    "Eduarda Fernandes":{
        "telefone": "4500-7800"
    },
    "Daniel Soares":{
        "telefone": "1245-9876"
    },
    "Jaqueline Matos":{
        "telefone": "3456-0976"
    }
}

listaPessoas.append(dados_pessoas)
sleep(0.4)
print(f"A lista contem as seguintes pessoas: \n{listaPessoas}\n",flush=True)

nome = input("Digite o nome: ")

if nome in dados_pessoas:
    sleep(0.4)
    detalhes = dados_pessoas[nome]
    print(f"Telefone: {detalhes["telefone"]}",flush=True)
else:
    print(f"A pessoa com o nome {nome} não foi encontrada.")
sleep(0.4)
print("PROGRAMA FINALIZADO...")