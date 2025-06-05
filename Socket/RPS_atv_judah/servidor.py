import socket
import os

# Configuração do servidor
HOST = 'localhost'  # Endereço do servidor
PORT = 12345        # Porta de comunicação
ARQUIVO_DADOS = "cpfs_e_nomes_e_idades.txt" # Novo nome do arquivo

# Criar socket do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    servidor.bind((HOST, PORT))
    servidor.listen(1)

    print(f"Servidor aguardando conexões em {HOST}:{PORT}...")

    # Aceitar conexão do cliente
    conn, addr = servidor.accept()
    print(f"Conexão estabelecida com {addr}")

    # Ler arquivo de CPFs, Nomes e Idades
    dados_usuarios = {} # Dicionário para armazenar CPF -> (Nome, Idade)
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    try:
                        cpf, nome, idade = linha.split(';', 2) # Divide em 3 partes
                        dados_usuarios[cpf.strip()] = (nome.strip(), idade.strip()) # Armazena como tupla (Nome, Idade)
                    except ValueError:
                        print(f"AVISO: Formato inválido na linha do arquivo '{ARQUIVO_DADOS}': {linha}. Linha ignorada.")
        print(f"Dados carregados do arquivo '{ARQUIVO_DADOS}': {dados_usuarios}")
    else:
        print(f"AVISO: O arquivo '{ARQUIVO_DADOS}' não foi encontrado. Nenhum dado será validado.")

    while True:
        cpf_cliente_raw = conn.recv(1024)
        if not cpf_cliente_raw:
            print("Cliente desconectou abruptamente.")
            break

        cpf_cliente = cpf_cliente_raw.decode().strip()

        if cpf_cliente.lower() == "sair":
            print(f"Cliente {addr} desconectou.")
            break

        print(f"Recebido CPF: {cpf_cliente} do cliente {addr}")

        # Verifica se o CPF está no dicionário e recupera nome e idade
        if cpf_cliente in dados_usuarios:
            nome_associado, idade_associada = dados_usuarios[cpf_cliente]
            resposta = f"Bom dia, {nome_associado}! Seu CPF ({cpf_cliente}) foi validado com sucesso. Idade: {idade_associada} anos."
        else:
            resposta = f"CPF ({cpf_cliente}) não encontrado ou inválido."

        conn.send(resposta.encode())

except OSError as e:
    if e.errno == 98:
        print(f"Erro: A porta {PORT} já está em uso. Por favor, feche outras instâncias ou tente outra porta.")
    else:
        print(f"Ocorreu um erro de SO no servidor: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado no servidor: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()
        print("Conexão com o cliente encerrada.")
    if servidor:
        servidor.close()
        print("Servidor encerrado.")