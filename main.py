import os
import sys
import subprocess

def display_menu():
    """Exibe o menu principal"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print("     SISTEMA DE VALIDAÇÃO DE CPF (TCP/UDP)")
    print("="*50)
    print("\nEscolha uma opção:")
    print("1. Iniciar Servidor TCP")
    print("2. Iniciar Cliente TCP")
    print("3. Iniciar Servidor UDP")
    print("4. Iniciar Cliente UDP")
    print("5. Sair")
    print("\nDigite o número da opção desejada:")

def start_program(script_name):
    """Inicia um programa em um novo processo"""
    try:
        # Inicia o script especificado em um novo processo
        subprocess.Popen([sys.executable, script_name])
        print(f"Iniciando {script_name}...")
        input("Pressione ENTER para voltar ao menu...")
    except Exception as e:
        print(f"Erro ao iniciar {script_name}: {e}")
        input("Pressione ENTER para continuar...")

def main():
    """Função principal que controla o fluxo do programa"""
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
            print("\nSaindo do programa...")
            sys.exit(0)
            
        else:
            print("\nOpção inválida! Pressione ENTER para tentar novamente...")
            input()

if __name__ == "__main__":
    main()
