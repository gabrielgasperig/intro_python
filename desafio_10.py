# --- Constantes para as regras da senha ---
COMPRIMENTO_MINIMO = 8
SIMBOLOS_PERMITIDOS = "!@#$%"

def validar_regras_senha(senha: str) -> list[str]:
    """
    Verifica se uma senha atende a um conjunto de regras de segurança.

    Em vez de retornar apenas True/False, retorna uma lista de mensagens
    de erro. Se a lista estiver vazia, a senha é válida.

    Args:
        senha (str): A senha a ser validada.

    Returns:
        list[str]: Uma lista contendo as mensagens de erro. Vazia se a senha
                   for válida.
    """
    erros = []
    
    if len(senha) < COMPRIMENTO_MINIMO:
        erros.append(f"Deve ter no mínimo {COMPRIMENTO_MINIMO} caracteres.")
        
    if not any(c.islower() for c in senha):
        erros.append("Deve conter pelo menos uma letra minúscula.")
        
    if not any(c.isupper() for c in senha):
        erros.append("Deve conter pelo menos uma letra maiúscula.")
        
    if not any(c.isdigit() for c in senha):
        erros.append("Deve conter pelo menos um número.")
        
    if not any(c in SIMBOLOS_PERMITIDOS for c in senha):
        erros.append(f"Deve conter um dos símbolos: {SIMBOLOS_PERMITIDOS}")
        
    return erros

def executar_desafio_10():
    """
    Executa o desafio 10, solicitando e validando uma senha do usuário.
    """
    print("\n--- Desafio 10: Validador de Senha Segura ---")
    print("Defina sua nova senha seguindo as regras abaixo:")
    print(f"- Mínimo de {COMPRIMENTO_MINIMO} caracteres")
    print("- Pelo menos 1 letra maiúscula (A-Z)")
    print("- Pelo menos 1 letra minúscula (a-z)")
    print("- Pelo menos 1 número (0-9)")
    print(f"- Pelo menos 1 símbolo ({SIMBOLOS_PERMITIDOS})")
    
    senha_usuario = input("\nDigite a senha: ")
    
    lista_de_erros = validar_regras_senha(senha_usuario)
    
    if not lista_de_erros:
        print("Senha válida!")
    else:
        print("Senha inválida.")
        for erro in lista_de_erros:
            print(f"- {erro}")