import socket
import sys

def validate_cpf_udp(cpf, host='localhost', port=65433):
    """
    Envia um CPF para validação no servidor UDP
    
    Args:
        cpf (str): CPF a ser validado
        host (str): Nome do host ou IP do servidor
        port (int): Porta do servidor
    
    Returns:
        str: Resposta do servidor
    """
    # Criar socket UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(5)  # Definir o tempo de espera para evitar bloqueios
    
    try:
        # Enviar CPF
        client.sendto(cpf.encode(), (host, port))
        
        # Receber resposta
        response, _ = client.recvfrom(1024)
        return response.decode()
        
    except socket.timeout:
        return "ERRO: Tempo de resposta excedido."
    except Exception as e:
        return f"ERRO: {str(e)}"
    finally:
        client.close()

def main():
    """Função principal para o cliente UDP"""
    print("Cliente de Validação de CPF UDP")
    print("="*30)
    
    # Obter detalhes do servidor (com valores padrão)
    host = input("Digite o nome do host do servidor (padrão: localhost): ").strip() or 'localhost'
    
    try:
        port_input = input("Digite a porta do servidor (padrão: 65433): ").strip()
        port = int(port_input) if port_input else 65433
    except ValueError:
        print("Número de porta inválido. Usando o valor padrão: 65433")
        port = 65433
    
    print(f"\nConectando a {host}:{port}")
    print("Digite 'exit' para sair")
    
    while True:
        # Obter CPF do usuário
        cpf = input("\nDigite o CPF para validação: ")
        
        if cpf.lower() == 'exit':
            print("Saindo...")
            break
            
        # Enviar CPF para validação
        print(f"Enviando CPF: {cpf}")
        response = validate_cpf_udp(cpf, host, port)
        print(f"Resposta do servidor: {response}")

if __name__ == "__main__":
    main()
