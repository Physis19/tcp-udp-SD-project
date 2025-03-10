import socket
import signal
import sys
from cpf_validator import validate_cpf

# Global variables for clean shutdown
server_socket = None

def signal_handler(sig, frame):
    """Handle keyboard interrupts gracefully"""
    print("\nServer shutting down...")
    if server_socket:
        server_socket.close()
    sys.exit(0)

def main():
    """Main function that runs the UDP server"""
    global server_socket
    
    host = 'localhost'
    port = 65433
    
    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Allow port reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        try:
            server_socket.bind((host, port))
        except socket.error as e:
            if e.errno == 98 or e.errno == 10048:  # Address already in use (Linux/Windows)
                print(f"Error: Port {port} is already in use.")
                print("Please choose a different port or stop the existing server.")
                alt_port = port + 1
                print(f"Attempting to use alternative port {alt_port}...")
                try:
                    server_socket.bind((host, alt_port))
                    port = alt_port
                    print(f"Successfully bound to alternative port {port}")
                except socket.error:
                    print("Alternative port also unavailable. Exiting.")
                    sys.exit(1)
            else:
                print(f"Socket error: {e}")
                sys.exit(1)
        
        print(f"UDP Server started on {host}:{port}")
        print("Waiting for CPF validation requests...")
        
        while True:
            # Receive data
            data, address = server_socket.recvfrom(1024)
            cpf = data.decode()
            
            print(f"Connection from {address}")
            print(f"CPF received: {cpf}")
            
            # Validate CPF
            result = "Valid CPF" if validate_cpf(cpf) else "Invalid CPF"
            print(f"Result: {result}")
            
            # Send response
            server_socket.sendto(result.encode(), address)
    
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        if server_socket:
            server_socket.close()
            print("Server socket closed")

if __name__ == "__main__":
    main()