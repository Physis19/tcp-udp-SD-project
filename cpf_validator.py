def validate_cpf(cpf):
    """
    Function that validates a CPF according to Brazilian Federal Revenue rules.
    
    Args:
        cpf (str): CPF number to be validated (with or without formatting)
    
    Returns:
        bool: True if the CPF is valid, False otherwise
    """
    # Remove non-numeric characters
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Check if it has 11 digits and is not a repeated sequence
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Calculate verification digits
    def calculate_digit(partial_cpf, weight):
        total = sum(int(digit) * w for digit, w in zip(partial_cpf, weight))
        remainder = total % 11
        return '0' if remainder < 2 else str(11 - remainder)

    # Calculate first digit
    first_digit = calculate_digit(cpf[:9], range(10, 1, -1))
    
    # Calculate second digit
    second_digit = calculate_digit(cpf[:10], range(11, 1, -1))

    # Check if calculated digits match the provided digits
    return cpf[-2:] == first_digit + second_digit