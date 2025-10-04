from utils import obter_float

def classificar_triangulo(lado1: float, lado2: float, lado3: float) -> str:
    """
    Verifica se três lados formam um triângulo e o classifica.

    A condição de existência de um triângulo é que a soma de quaisquer
    dois lados seja maior que o terceiro lado.

    Args:
        lado1 (float): O comprimento do primeiro lado.
        lado2 (float): O comprimento do segundo lado.
        lado3 (float): O comprimento do terceiro lado.

    Returns:
        str: A classificação do triângulo ("Equilátero", "Isósceles", 
             "Escaleno"), ou uma mensagem indicando que não forma um 
             triângulo ou que os valores são inválidos.
    """
    # Validação de valores positivos
    if not (lado1 > 0 and lado2 > 0 and lado3 > 0):
        return "Valores inválidos. Os lados devem ser maiores que zero."

    # Condição de existência de um triângulo
    if not (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
        return "Não forma um triângulo."

    # Classificação do triângulo
    if lado1 == lado2 == lado3:
        return "O triângulo é Equilátero."
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return "O triângulo é Isósceles."
    else:
        return "O triângulo é Escaleno."

def executar_desafio_02():
    """
    Executa o desafio 2, solicitando os lados de um triângulo ao usuário
    e imprimindo sua classificação.
    """
    print("\n--- Desafio 2: Classificação de Triângulos ---")
    
    l1 = obter_float("Digite o comprimento do lado 1: ")
    l2 = obter_float("Digite o comprimento do lado 2: ")
    l3 = obter_float("Digite o comprimento do lado 3: ")
    
    resultado = classificar_triangulo(l1, l2, l3)
    print(resultado)