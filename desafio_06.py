from utils import obter_int, obter_int_no_intervalo

def verificar_situacao_voto(idade: int, nacionalidade: str) -> str:
    """
    Verifica a situação de voto de uma pessoa com base na idade e nacionalidade.

    Args:
        idade (int): A idade da pessoa.
        nacionalidade (str): A nacionalidade ("brasileiro" ou "estrangeiro").

    Returns:
        str: A string descrevendo a situação de voto.
    """
    if idade < 16:
        return "Não pode votar."
    
    # Para estrangeiros, o voto é sempre opcional a partir dos 16 anos.
    if nacionalidade == 'estrangeiro':
        return "Voto opcional para estrangeiros."
        
    # Para brasileiros, o voto é opcional entre 16 e 18 anos.
    if 16 <= idade < 18 or idade > 70: # Voto também é opcional para maiores de 70
        return "Voto opcional."
    
    # Se chegou aqui, idade >= 18 e <= 70 e é brasileiro
    return "Voto obrigatório."

def executar_desafio_06():
    """
    Executa o desafio 6, perguntando idade e nacionalidade para
    determinar a situação de voto.
    """
    print("\n--- Desafio 6: Verificação de Voto ---")
    
    # Garante que a idade seja um número positivo
    idade = obter_int("Qual é a sua idade? ")
    while idade < 0:
        print("Idade inválida.")
        idade = obter_int("Digite uma idade válida: ")

    menu_nacionalidade = (
        "Selecione a sua nacionalidade:\n"
        "1 - Brasileiro\n"
        "2 - Estrangeiro\n"
        "Opção: "
    )
    opcao = obter_int_no_intervalo(menu_nacionalidade, 1, 2)
    
    nacionalidade = 'brasileiro' if opcao == 1 else 'estrangeiro'
    
    situacao = verificar_situacao_voto(idade, nacionalidade)
    print(f"Situação: {situacao}")