from utils import obter_int

def _eh_ano_bissexto(ano: int) -> bool:
    """
    Verifica se um ano é bissexto.
    Um ano é bissexto se for divisível por 4, exceto para anos que são
    divisíveis por 100 mas não por 400.
    """
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def eh_data_valida(dia: int, mes: int, ano: int) -> bool:
    """
    Verifica se uma data (dia, mês, ano) é válida.

    Args:
        dia (int): O dia do mês.
        mes (int): O mês do ano (1-12).
        ano (int): O ano.

    Returns:
        bool: True se a data for válida, False se for inválida.
    """
    # Checagens básicas
    if not (1 <= mes <= 12 and ano > 0 and dia > 0):
        return False
    
    # Define o número máximo de dias para o mês
    if mes in [4, 6, 9, 11]:
        dias_no_mes = 30
    elif mes == 2:
        dias_no_mes = 29 if _eh_ano_bissexto(ano) else 28
    else:
        dias_no_mes = 31
        
    return dia <= dias_no_mes

def executar_desafio_05():
    """
    Executa o desafio 5, solicitando uma data ao usuário e
    informando se ela é válida ou não.
    """
    print("\n--- Desafio 5: Validador de Datas ---")
    
    ano = obter_int("Digite o ano: ")
    mes = obter_int("Digite o mês: ")
    dia = obter_int("Digite o dia: ")
    
    if eh_data_valida(dia, mes, ano):
        print(f"A data {dia:02d}/{mes:02d}/{ano} é VÁLIDA.")
    else:
        print(f"A data {dia:02d}/{mes:02d}/{ano} é INVÁLIDA.")