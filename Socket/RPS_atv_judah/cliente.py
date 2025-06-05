import socket

# Configuração do cliente
HOST = 'localhost'  # Endereço do servidor
PORT = 12345        # Porta de comunicação

# Criar socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect((HOST, PORT))
    print("Conectado ao servidor.\nDigite seu CPF para validar ou 'sair' para encerrar.")

    while True:
        cpf = input("Digite seu CPF (formato XXX.XXX.XXX-XX): ")
        cliente.send(cpf.encode())

        if cpf.lower() == "sair":
            print("Encerrando conexão...")
            break

        resposta = cliente.recv(1024).decode()
        print(f"Servidor: {resposta}")

except ConnectionRefusedError:
    print(f"Erro: Conexão recusada. Certifique-se de que o servidor está rodando em {HOST}:{PORT}")
except Exception as e:
    print(f"Ocorreu um erro inesperado no cliente: {e}")
finally:
    # Fechar conexão
    cliente.close()
    print("Conexão encerrada.")