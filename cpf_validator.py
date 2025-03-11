def validate_cpf(cpf):
    """
    Função que valida um CPF de acordo com as regras da Receita Federal Brasileira.
    
    Args:
        cpf (str): Número do CPF a ser validado (com ou sem formatação)
    
    Returns:
        bool: True se o CPF for válido, False caso contrário
    """
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF tem 11 dígitos e não é uma sequência repetida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Função para calcular o dígito de verificação
    def calculate_digit(partial_cpf, weight):
        total = sum(int(digit) * w for digit, w in zip(partial_cpf, weight))
        remainder = total % 11
        return '0' if remainder < 2 else str(11 - remainder)

    # Calcula o primeiro dígito
    first_digit = calculate_digit(cpf[:9], range(10, 1, -1))
    
    # Calcula o segundo dígito
    second_digit = calculate_digit(cpf[:10], range(11, 1, -1))

    # Verifica se os dígitos calculados coincidem com os fornecidos
    return cpf[-2:] == first_digit + second_digit
