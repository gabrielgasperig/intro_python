from utils import obter_int, obter_float_positivo

def classificar_risco_financeiro(renda: float, dividas: float) -> str:
    """
    Classifica o risco financeiro de uma pessoa com base em sua renda e dívidas.

    Args:
        renda (float): A renda mensal da pessoa.
        dividas (float): O valor total das dívidas da pessoa.

    Returns:
        str: A classificação de risco ("Alta", "Média", "Baixa", "Médio-baixo").
    """
    # Evita divisão por zero se a renda for 0
    if renda <= 0:
        return "Alta" if dividas > 0 else "Baixa"

    percentual_divida = dividas / renda
    
    # As regras são verificadas em ordem de especificidade
    if renda > 5000 and percentual_divida < 0.30:
        return "Baixa"
    elif renda < 2000 and percentual_divida > 0.50:
        return "Alta"
    elif (2000 <= renda <= 5000) or (0.30 <= percentual_divida <= 0.50):
        return "Média"
    else:
        return "Médio-baixo"

def executar_desafio_07():
    """
    Executa o desafio 7, solicitando dados financeiros para
    realizar uma classificação de risco.
    """
    print("\n--- Desafio 7: Classificação de Risco Financeiro ---")
    
    # A idade é solicitada, mas não entra no cálculo de risco.
    _ = obter_int("Digite a sua idade: ")
    
    renda = obter_float_positivo("Digite a sua renda mensal: R$")
    dividas = obter_float_positivo("Digite o seu débito total: R$")
    
    risco = classificar_risco_financeiro(renda, dividas)
    print(f"Resultado: Classificação de risco {risco}.")