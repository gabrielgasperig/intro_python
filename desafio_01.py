from utils import obter_float, obter_int

def calcular_bonus(salario: float, tempo_empresa: int) -> float:
    """Calcula o bônus de um funcionário com base no salário e tempo de empresa.

    Args:
        salario (float): O valor do salário do funcionário.
        tempo_empresa (int): O número de anos completos na empresa.

    Returns:
        float: O valor do bônus calculado. Retorna 0 se não houver bônus.
    """
    if salario < 2000:
        if tempo_empresa >= 5:
            return salario * 0.20  # Bônus de 20%
        else:
            return salario * 0.10  # Bônus de 10%
    else:  # Salário >= 2000
        if tempo_empresa >= 5:
            return salario * 0.05  # Bônus de 5%
        else:
            return 0.0  # Sem bônus

def executar_desafio_01():
    """
    Executa o desafio 1, solicitando os dados do usuário e imprimindo o bônus.
    """
    print("\n--- Desafio 1: Cálculo de Bônus ---")
    salario = obter_float("Digite seu salário: ")
    tempo = obter_int("Digite o tempo de empresa (em anos): ")
    
    bonus = calcular_bonus(salario, tempo)
    
    if bonus > 0:
        # A função format() com 'f' garante a formatação como moeda.
        print(f"Você recebeu um bônus de R$ {bonus:.2f}")
    else:
        print("Você não tem direito a bônus desta vez.")