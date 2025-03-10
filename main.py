import os
import sys
import subprocess

def display_menu():
    """Displays the main menu"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print("     CPF VALIDATION SYSTEM (TCP/UDP)")
    print("="*50)
    print("\nChoose an option:")
    print("1. Start TCP Server")
    print("2. Start TCP Client")
    print("3. Start UDP Server")
    print("4. Start UDP Client")
    print("5. Exit")
    print("\nEnter the number of the desired option:")

def start_program(script_name):
    """Start a program in a new process"""
    try:
        # Start the specified script in a new process
        subprocess.Popen([sys.executable, script_name])
        print(f"Starting {script_name}...")
        input("Press ENTER to return to menu...")
    except Exception as e:
        print(f"Error starting {script_name}: {e}")
        input("Press ENTER to continue...")

def main():
    """Main function that controls program flow"""
    while True:
        display_menu()
        option = input().strip()
        
        if option == '1':
            start_program('tcp_server.py')
            
        elif option == '2':
            start_program('tcp_client.py')
            
        elif option == '3':
            start_program('udp_server.py')
            
        elif option == '4':
            start_program('udp_client.py')
            
        elif option == '5':
            print("\nExiting program...")
            sys.exit(0)
            
        else:
            print("\nInvalid option! Press ENTER to try again...")
            input()

if __name__ == "__main__":
    main()