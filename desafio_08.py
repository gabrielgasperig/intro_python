from utils import obter_char_valido

GABARITO_CARTAS = ['B', 'C', 'D', 'A']
PONTUACAO_MAXIMA = 50
CARTAS_VALIDAS = ['A', 'B', 'C', 'D']

def calcular_pontuacao_cartas(resposta: list[str], gabarito: list[str]) -> int:
    """
    Calcula a pontuação de uma sequência de cartas com base em regras específicas.

    Regras de pontuação:
    - 10 pontos por acerto na posição correta.
    - 5 pontos de bônus para cada carta 'A' na resposta.
    - 5 pontos de bônus se 'C' for seguido por 'D' na resposta.
    - A pontuação máxima é 50.

    Args:
        resposta (list[str]): A sequência de 4 cartas do usuário.
        gabarito (list[str]): A sequência correta de cartas.

    Returns:
        int: A pontuação final calculada.
    """
    pontos = 0
    
    # Regra a: 10 pontos por acerto
    # Regra b: Bônus de 5 pontos para cada 'A'
    for i in range(len(gabarito)):
        if resposta[i] == gabarito[i]:
            pontos += 10
        if resposta[i] == 'A':
            pontos += 5
            
    # Regra c: Bônus de 5 pontos para a sequência 'C' -> 'D'
    for i in range(len(resposta) - 1):
        if resposta[i] == 'C' and resposta[i+1] == 'D':
            pontos += 5
            
    # Garante que a pontuação não exceda o máximo
    return min(pontos, PONTUACAO_MAXIMA)

def executar_desafio_08():
    """
    Executa o desafio 8, o jogo de adivinhar a sequência de cartas.
    """
    print("\n--- Desafio 8: Jogo de Cartas ---")
    print(f"Adivinhe a sequência de 4 cartas. Opções: {', '.join(CARTAS_VALIDAS)}")
    
    resposta_usuario = []
    for i in range(4):
        carta = obter_char_valido(
            f"Digite a carta da posição {i + 1}: ",
            opcoes_validas=CARTAS_VALIDAS
        )
        resposta_usuario.append(carta)
        
    pontuacao = calcular_pontuacao_cartas(resposta_usuario, GABARITO_CARTAS)
    
    print(f"\nSua sequência: {resposta_usuario}")
    print(f"Sequência correta: {GABARITO_CARTAS}")
    print(f"Sua pontuação final: {pontuacao} pontos.")

def obter_char_valido(mensagem: str, opcoes_validas: list[str]) -> str:
    """
    Solicita um único caractere ao usuário, garantindo que ele esteja
    em uma lista de opções válidas.

    Args:
        mensagem (str): A mensagem a ser exibida para o usuário.
        opcoes_validas (list[str]): Uma lista de strings com os caracteres
                                    aceitáveis (serão comparados em maiúsculo).

    Returns:
        str: O caractere validado em maiúsculo.
    """
    # Garante que a comparação seja sempre com maiúsculas
    opcoes_maiusculas = [opt.upper() for opt in opcoes_validas]
    
    while True:
        entrada = input(mensagem).strip().upper()
        if entrada in opcoes_maiusculas:
            return entrada
        else:
            print(f"Entrada inválida. Use uma das opções: {', '.join(opcoes_maiusculas)}")