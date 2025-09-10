'''
O sistema solicita uma senha ao usuário, informando as regras, e exibe senha
válida se as seguintes regras forem atendidas:
a. Mínimo 8 caracteres
b. Contém pelo menos 1 maiúscula, 1 minúscula, 1 número e 1 dos seguintes
símbolos: !@#$%
'''

def validar_senha():
    print("Regras para a senha:")
    print("- Mínimo 8 caracteres")
    print("- Pelo menos 1 maiúscula, 1 minúscula, 1 número e 1 símbolo (!@#$%)")
    senha = input("Digite a senha: ")

    if (
        len(senha) >= 8
        and any(c.isupper() for c in senha)
        and any(c.islower() for c in senha)
        and any(c.isdigit() for c in senha)
        and any(c in "!@#$%" for c in senha)
    ):
        print("Senha válida")
    else:
        print("Senha inválida")

validar_senha()