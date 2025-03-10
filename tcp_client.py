import socket
import sys

def validate_cpf_tcp(cpf, host='localhost', port=65432):
    """
    Sends a CPF for validation to the TCP server
    
    Args:
        cpf (str): CPF to be validated
        host (str): Server hostname or IP
        port (int): Server port
    
    Returns:
        str: Server response
    """
    # Create TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)  # Set timeout to prevent hanging
    
    try:
        # Connect to server
        client.connect((host, port))
        
        # Send CPF
        client.sendall(cpf.encode())
        
        # Receive response
        response = client.recv(1024).decode()
        return response
        
    except ConnectionRefusedError:
        return "ERROR: Could not connect to server."
    except socket.timeout:
        return "ERROR: Server response timeout."
    except Exception as e:
        return f"ERROR: {str(e)}"
    finally:
        client.close()

def main():
    """Main function for the TCP client"""
    print("CPF Validation TCP Client")
    print("="*30)
    
    # Get server details (with defaults)
    host = input("Enter server hostname (default: localhost): ").strip() or 'localhost'
    
    try:
        port_input = input("Enter server port (default: 65432): ").strip()
        port = int(port_input) if port_input else 65432
    except ValueError:
        print("Invalid port number. Using default: 65432")
        port = 65432
    
    print(f"\nConnecting to {host}:{port}")
    print("Type 'exit' to quit")
    
    while True:
        # Get CPF from user
        cpf = input("\nEnter CPF for validation: ")
        
        if cpf.lower() == 'exit':
            print("Exiting...")
            break
            
        # Send CPF for validation
        print(f"Sending CPF: {cpf}")
        response = validate_cpf_tcp(cpf, host, port)
        print(f"Server response: {response}")

if __name__ == "__main__":
    main()