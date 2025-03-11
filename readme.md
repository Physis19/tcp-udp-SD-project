# Sistema de Validação de CPF (TCP/UDP)

Este projeto implementa um sistema distribuído para validação de CPF (Cadastro de Pessoas Físicas) utilizando dois protocolos diferentes: TCP e UDP. O sistema consiste em programas de cliente e servidor independentes para cada protocolo, permitindo a comunicação em rede para validação de números de CPF.

## Estrutura do Projeto

O projeto está estruturado em componentes separados e independentes:

- `cpf_validator.py`: Módulo com a lógica de validação de CPF
- `tcp_server.py`: Servidor que valida CPFs usando o protocolo TCP
- `tcp_client.py`: Cliente que envia CPFs para validação usando o protocolo TCP
- `udp_server.py`: Servidor que valida CPFs usando o protocolo UDP
- `udp_client.py`: Cliente que envia CPFs para validação usando o protocolo UDP

## Funcionamento Detalhado

### Validação de CPF (`cpf_validator.py`)

Este módulo contém a função `validate_cpf(cpf)` que implementa a lógica de validação de acordo com as regras da Receita Federal Brasileira. A validação inclui:

- Verificação do formato (11 dígitos)
- Cálculo e verificação dos dígitos verificadores
- Rejeição de sequências repetitivas (ex: 11111111111)

### Servidor TCP (`tcp_server.py`)

O servidor TCP:
- Inicializa em `localhost:65432` por padrão
- Aceita conexões de clientes TCP
- Recebe strings de CPF
- Valida os CPFs recebidos
- Retorna "Valid CPF" ou "Invalid CPF" para o cliente
- Trata erros graciosamente, incluindo tentativas automáticas de usar portas alternativas quando a porta padrão está ocupada
- Registra toda a atividade no console

### Cliente TCP (`tcp_client.py`)

O cliente TCP:
- Conecta-se ao servidor TCP (padrão: `localhost:65432`)
- Permite ao usuário inserir um CPF para validação
- Envia o CPF ao servidor
- Exibe a resposta do servidor
- Implementa timeout para evitar bloqueio indefinido
- Trata erros de conexão e comunicação

### Servidor UDP (`udp_server.py`)

O servidor UDP:
- Inicializa em `localhost:65433` por padrão
- Escuta datagramas UDP contendo CPFs para validação
- Valida os CPFs recebidos
- Retorna "Valid CPF" ou "Invalid CPF" como resposta
- Implementa tratamento de portas ocupadas (tenta automaticamente usar a porta seguinte)
- Registra toda a atividade no console

### Cliente UDP (`udp_client.py`)

O cliente UDP:
- Conecta-se ao servidor UDP (padrão: `localhost:65433`)
- Permite ao usuário inserir um CPF para validação
- Envia o CPF ao servidor em um datagrama UDP
- Exibe a resposta do servidor
- Implementa timeout para evitar bloqueio indefinido
- Trata erros de comunicação


## Como Executar

Para executar o sistema, você precisa iniciar o servidor e o cliente correspondente em janelas de terminal separadas:

### Executando o Servidor TCP:
```bash
python tcp_server.py
```
O servidor TCP iniciará na porta 65432. Se essa porta estiver ocupada, ele tentará automaticamente usar a porta 65433.

### Executando o Cliente TCP:
```bash
python tcp_client.py
```
O cliente solicitará o host e porta do servidor (pressione Enter para usar os valores padrão) e então permitirá que você digite CPFs para validação.

### Executando o Servidor UDP:
```bash
python udp_server.py
```
O servidor UDP iniciará na porta 65433. Se essa porta estiver ocupada, ele tentará automaticamente usar a porta 65434.

### Executando o Cliente UDP:
```bash
python udp_client.py
```
O cliente solicitará o host e porta do servidor (pressione Enter para usar os valores padrão) e então permitirá que você digite CPFs para validação.

## Tratamento de Erros

O sistema implementa tratamento robusto de erros, incluindo:

- **Portas ocupadas**: Servidores tentam automaticamente usar portas alternativas
- **Timeouts**: Clientes não bloqueiam indefinidamente esperando resposta
- **Conexões recusadas**: Mensagens de erro claras quando não é possível conectar
- **Interrupções**: Gerenciamento adequado de sinais como SIGINT (Ctrl+C)

## Exemplos de Uso

### Validação de CPF Válido
```
Enter CPF for validation: 529.982.247-25
Server response: Valid CPF
```

### Validação de CPF Inválido
```
Enter CPF for validation: 123.456.789-00
Server response: Invalid CPF
```

### Saída do Programa
```
Enter CPF for validation: exit
Exiting...
```

## Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca adicional necessária (utiliza apenas módulos da biblioteca padrão Python)
- Sistemas operacionais suportados: Windows, Linux, macOS

## Considerações Técnicas

- **Sockets**: Implementação baseada na biblioteca `socket` padrão do Python
- **Tratamento de Sinais**: Gerenciamento adequado de sinais para encerramento limpo
- **Codificação**: Comunicação usando codificação UTF-8
- **Reutilização de Portas**: Configuração de sockets para permitir reutilização de portas (SO_REUSEADDR)
