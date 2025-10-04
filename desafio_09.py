from utils import obter_float_positivo, obter_int_no_intervalo

def calcular_preco_final(preco_original: float, eh_vip: bool) -> tuple[float, float]:
    """
    Calcula o desconto e o preço final de um produto com base no preço
    e no status VIP do cliente.

    Regras de desconto:
    - Preço >= 100: 20%
    - Preço >= 50:  10%
    - Cliente VIP:  +5% adicional

    Args:
        preco_original (float): O preço do produto.
        eh_vip (bool): True se o cliente for VIP, False caso contrário.

    Returns:
        tuple[float, float]: Uma tupla contendo (valor_do_desconto, preco_final).
    """
    percentual_desconto = 0.0
    
    # Desconto baseado no preço
    if preco_original >= 100:
        percentual_desconto = 0.20
    elif preco_original >= 50:
        percentual_desconto = 0.10
        
    # Desconto adicional para cliente VIP
    if eh_vip:
        percentual_desconto += 0.05
        
    valor_do_desconto = preco_original * percentual_desconto
    preco_final = preco_original - valor_do_desconto
    
    return (valor_do_desconto, preco_final)

def executar_desafio_09():
    """
    Executa o desafio 9, solicitando o preço e status do cliente para
    calcular o desconto.
    """
    print("\n--- Desafio 9: Calculadora de Descontos ---")
    
    preco = obter_float_positivo("Digite o valor do produto: R$")
    
    menu_vip = (
        "Você é cliente VIP?\n"
        "1 - Sim\n"
        "0 - Não\n"
        "Opção: "
    )
    opcao_vip = obter_int_no_intervalo(menu_vip, 0, 1)
    cliente_eh_vip = bool(opcao_vip) # Converte 1 para True, 0 para False
    
    desconto, valor_final = calcular_preco_final(preco, cliente_eh_vip)
    
    if desconto > 0:
        print(f"\nDesconto total: R$ {desconto:.2f}")
    else:
        print("\nEste produto não possui desconto.")
        
    print(f"Valor final a pagar: R$ {valor_final:.2f}")