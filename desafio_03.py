from utils import obter_float

def calcular_imc(peso: float, altura: float) -> float | None:
    """Calcula o Índice de Massa Corporal (IMC).

    Args:
        peso (float): O peso da pessoa em quilogramas (kg).
        altura (float): A altura da pessoa em metros (m).

    Returns:
        float | None: O valor do IMC calculado. Retorna None se a altura for 0
                      ou se os valores de peso/altura forem inválidos.
    """
    if altura <= 0 or peso <= 0:
        return None
    return peso / (altura ** 2)

def classificar_imc(imc: float) -> str:
    """Retorna a classificação do IMC com base em seu valor.

    Args:
        imc (float): O valor do IMC a ser classificado.

    Returns:
        str: A string contendo a classificação do IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade Grau I"
    elif imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

def executar_desafio_03():
    """
    Executa o desafio 3, solicitando peso e altura, calculando o IMC
    e exibindo a classificação.
    """
    print("\n--- Desafio 3: Cálculo e Classificação de IMC ---")
    
    peso = obter_float("Digite seu peso em kg: ")
    altura = obter_float("Digite sua altura em metros (ex: 1.75): ")

    imc_valor = calcular_imc(peso, altura)
    
    if imc_valor is not None:
        classificacao = classificar_imc(imc_valor)
        print(f"Seu IMC é {imc_valor:.2f}. Classificação: {classificacao}.")
    else:
        print("Valores de peso e altura inválidos. Tente novamente.")