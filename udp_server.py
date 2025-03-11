import socket
import signal
import sys
from cpf_validator import validate_cpf

# Variáveis globais para um desligamento limpo
server_socket = None

def signal_handler(sig, frame):
    """Tratar interrupções do teclado de forma graciosa"""
    print("\nServidor desligando...")
    if server_socket:
        server_socket.close()
    sys.exit(0)

def main():
    """Função principal que executa o servidor UDP"""
    global server_socket
    
    host = 'localhost'
    port = 65433
    
    # Registrar os manipuladores de sinais
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Criar o socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Permitir reutilização da porta
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        try:
            server_socket.bind((host, port))
        except socket.error as e:
            if e.errno == 98 or e.errno == 10048:  # Endereço já em uso (Linux/Windows)
                print(f"Erro: A porta {port} já está em uso.")
                print("Escolha uma porta diferente ou pare o servidor existente.")
                alt_port = port + 1
                print(f"Tentando usar a porta alternativa {alt_port}...")
                try:
                    server_socket.bind((host, alt_port))
                    port = alt_port
                    print(f"Conectado com sucesso à porta alternativa {port}")
                except socket.error:
                    print("A porta alternativa também está indisponível. Saindo.")
                    sys.exit(1)
            else:
                print(f"Erro no socket: {e}")
                sys.exit(1)
        
        print(f"Servidor UDP iniciado em {host}:{port}")
        print("Aguardando requisições de validação de CPF...")
        
        while True:
            # Receber dados
            data, address = server_socket.recvfrom(1024)
            cpf = data.decode()
            
            print(f"Conexão de {address}")
            print(f"CPF recebido: {cpf}")
            
            # Validar CPF
            result = "CPF válido" if validate_cpf(cpf) else "CPF inválido"
            print(f"Resultado: {result}")
            
            # Enviar resposta
            server_socket.sendto(result.encode(), address)
    
    except Exception as e:
        print(f"Erro no servidor: {e}")
    finally:
        if server_socket:
            server_socket.close()
            print("Socket do servidor fechado")

if __name__ == "__main__":
    main()
