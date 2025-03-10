import socket
import sys

def validate_cpf_udp(cpf, host='localhost', port=65433):
    """
    Sends a CPF for validation to the UDP server
    
    Args:
        cpf (str): CPF to be validated
        host (str): Server hostname or IP
        port (int): Server port
    
    Returns:
        str: Server response
    """
    # Create UDP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(5)  # Set timeout to prevent hanging
    
    try:
        # Send CPF
        client.sendto(cpf.encode(), (host, port))
        
        # Receive response
        response, _ = client.recvfrom(1024)
        return response.decode()
        
    except socket.timeout:
        return "ERROR: Response timeout exceeded."
    except Exception as e:
        return f"ERROR: {str(e)}"
    finally:
        client.close()

def main():
    """Main function for the UDP client"""
    print("CPF Validation UDP Client")
    print("="*30)
    
    # Get server details (with defaults)
    host = input("Enter server hostname (default: localhost): ").strip() or 'localhost'
    
    try:
        port_input = input("Enter server port (default: 65433): ").strip()
        port = int(port_input) if port_input else 65433
    except ValueError:
        print("Invalid port number. Using default: 65433")
        port = 65433
    
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
        response = validate_cpf_udp(cpf, host, port)
        print(f"Server response: {response}")

if __name__ == "__main__":
    main()