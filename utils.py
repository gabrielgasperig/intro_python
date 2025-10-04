def obter_float(mensagem: str) -> float:
    """Solicita um número de ponto flutuante (decimal) ao usuário.

    Args:
        mensagem (str): A mensagem a ser exibida para o usuário.

    Returns:
        float: O número digitado pelo usuário.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def obter_int(mensagem: str) -> int:
    """Solicita um número inteiro ao usuário.

    Args:
        mensagem (str): A mensagem a ser exibida para o usuário.

    Returns:
        int: O número digitado pelo usuário.
    """
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def obter_nota_valida(mensagem: str) -> float:
    """
    Solicita uma nota ao usuário, garantindo que seja um número
    entre 0 e 10.

    Args:
        mensagem (str): A mensagem a ser exibida para o usuário.

    Returns:
        float: A nota validada.
    """
    while True:
        nota = obter_float(mensagem)
        if 0 <= nota <= 10:
            return nota
        else:
            print("Nota inválida. Por favor, digite um valor entre 0 e 10.")

def obter_int_no_intervalo(mensagem: str, minimo: int, maximo: int) -> int:
    """
    Solicita um número inteiro ao usuário, garantindo que esteja
    dentro de um intervalo [minimo, maximo].

    Args:
        mensagem (str): A mensagem a ser exibida para o usuário.
        minimo (int): O valor mínimo aceitável.
        maximo (int): O valor máximo aceitável.

    Returns:
        int: O número inteiro validado.
    """
    while True:
        numero = obter_int(mensagem)
        if minimo <= numero <= maximo:
            return numero
        else:
            print(f"Opção inválida. Por favor, digite um número entre {minimo} e {maximo}.")

def obter_float_positivo(mensagem: str) -> float:
    """
    Solicita um número de ponto flutuante (decimal) ao usuário,
    garantindo que seja positivo (>= 0).

    Args:
        mensagem (str): A mensagem a ser exibida para o usuário.

    Returns:
        float: O número validado.
    """
    while True:
        numero = obter_float(mensagem)
        if numero >= 0:
            return numero
        else:
            print("Valor inválido. Por favor, digite um número positivo.")

def obter_char_valido(mensagem: str, opcoes_validas: list[str]) -> str:
    """Solicita um char, garantindo que esteja em uma lista de opções."""
    opcoes_maiusculas = [opc.upper() for opc in opcoes_validas]
    while True:
        entrada = input(mensagem).strip().upper()
        if entrada in opcoes_maiusculas:
            return entrada
        else:
            print(f"Entrada inválida. Use uma das opções: {', '.join(opcoes_maiusculas)}")
