# Sistema de Validação de CPF (TCP/UDP)

Este projeto implementa um sistema distribuído para validação de CPF (Cadastro de Pessoas Físicas) utilizando dois protocolos diferentes: TCP e UDP. O sistema consiste em programas de cliente e servidor separados para cada protocolo.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- `cpf_validator.py`: Módulo com a função de validação de CPF
- `tcp_server.py`: Servidor TCP para validação de CPF
- `tcp_client.py`: Cliente TCP para envio de CPFs
- `udp_server.py`: Servidor UDP para validação de CPF
- `udp_client.py`: Cliente UDP para envio de CPFs
- `menu.py`: Interface para iniciar os diferentes componentes do sistema

## Como Executar

Você pode executar os componentes do sistema de duas maneiras:

### 1. Utilizando o Menu

Execute o `menu.py` para acessar uma interface que permite iniciar qualquer componente do sistema:

```
python menu.py
```

### 2. Executando os Componentes Diretamente

Cada componente pode ser executado independentemente:

**Servidor TCP:**
```
python tcp_server.py
```

**Cliente TCP:**
```
python tcp_client.py
```

**Servidor UDP:**
```
python udp_server.py
```

**Cliente UDP:**
```
python udp_client.py
```

## Características do Sistema

- **Distribuído**: Cliente e servidor são programas separados que se comunicam pela rede
- **Protocolos Independentes**: Implementações TCP e UDP completamente separadas
- **Validação de CPF**: Implementa validação de acordo com as regras da Receita Federal brasileira
- **Tratamento de Erros**: Gerenciamento adequado de timeouts e erros de conexão
- **Encerramento Limpo**: Sistema gerencia interrupções e libera recursos corretamente

## Requisitos

- Python 3.6+
- Nenhuma biblioteca adicional necessária (utiliza apenas módulos da biblioteca padrão)

## Funcionamento

1. Inicie o servidor (TCP ou UDP)
2. Em outra janela de terminal, inicie o cliente correspondente
3. No cliente, digite um CPF para validação
4. O servidor processará o CPF e retornará o resultado
5. Digite 'exit' no cliente para encerrar a aplicação
