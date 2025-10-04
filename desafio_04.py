from utils import obter_nota_valida

def calcular_situacao_aluno(nota1: float, nota2: float, nota3: float) -> tuple[float, str]:
    """
    Calcula a média de 3 notas e determina a situação do aluno.

    Regras:
    - Se qualquer nota for 0, o aluno é reprovado automaticamente.
    - Média >= 7: Aprovado
    - Média >= 5 e < 7: Recuperação
    - Média < 5: Reprovado

    Args:
        nota1 (float): Nota da primeira prova (0 a 10).
        nota2 (float): Nota da segunda prova (0 a 10).
        nota3 (float): Nota da terceira prova (0 a 10).

    Returns:
        tuple[float, str]: Uma tupla contendo a média calculada e a string
                           com a situação do aluno.
    """
    media = (nota1 + nota2 + nota3) / 3

    if nota1 == 0 or nota2 == 0 or nota3 == 0:
        return (media, "Reprovado (nota 0 elimina automaticamente).")
    
    if media >= 7:
        return (media, "Aprovado!")
    elif media >= 5:
        return (media, "Em recuperação.")
    else:
        return (media, "Reprovado. Estude mais!")

def executar_desafio_04():
    """
    Executa o desafio 4, solicitando as notas do aluno, calculando a média
    e exibindo a situação final.
    """
    print("\n--- Desafio 4: Boletim Escolar ---")
    
    n1 = obter_nota_valida("Digite a primeira nota (0 a 10): ")
    n2 = obter_nota_valida("Digite a segunda nota (0 a 10): ")
    n3 = obter_nota_valida("Digite a terceira nota (0 a 10): ")
    
    media, situacao = calcular_situacao_aluno(n1, n2, n3)
    
    print(f"\nSua média final é {media:.2f}.")
    print(f"Situação: {situacao}")