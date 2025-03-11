import socket
import sys

def validate_cpf_tcp(cpf, host='localhost', port=65432):
    """
    Envia um CPF para validação para o servidor TCP
    
    Args:
        cpf (str): CPF a ser validado
        host (str): Nome do host ou IP do servidor
        port (int): Porta do servidor
    
    Returns:
        str: Resposta do servidor
    """
    # Criar o socket TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)  # Definir o tempo limite para evitar travamento
    
    try:
        # Conectar ao servidor
        client.connect((host, port))
        
        # Enviar CPF
        client.sendall(cpf.encode())
        
        # Receber resposta
        response = client.recv(1024).decode()
        return response
        
    except ConnectionRefusedError:
        return "ERRO: Não foi possível conectar ao servidor."
    except socket.timeout:
        return "ERRO: Tempo de resposta do servidor excedido."
    except Exception as e:
        return f"ERRO: {str(e)}"
    finally:
        client.close()

def main():
    """Função principal para o cliente TCP"""
    print("Cliente de Validação de CPF TCP")
    print("="*30)
    
    # Obter os detalhes do servidor (com valores padrão)
    host = input("Digite o nome do servidor (padrão: localhost): ").strip() or 'localhost'
    
    try:
        port_input = input("Digite a porta do servidor (padrão: 65432): ").strip()
        port = int(port_input) if port_input else 65432
    except ValueError:
        print("Número de porta inválido. Usando o valor padrão: 65432")
        port = 65432
    
    print(f"\nConectando-se a {host}:{port}")
    print("Digite 'exit' para sair")
    
    while True:
        # Obter CPF do usuário
        cpf = input("\nDigite o CPF para validação: ")
        
        if cpf.lower() == 'exit':
            print("Saindo...")
            break
            
        # Enviar CPF para validação
        print(f"Enviando CPF: {cpf}")
        response = validate_cpf_tcp(cpf, host, port)
        print(f"Resposta do servidor: {response}")

if __name__ == "__main__":
    main()
