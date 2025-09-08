'''
O sistema solicita uma senha ao usuário, informando as regras, e exibe senha
válida se as seguintes regras forem atendidas:
a. Mínimo 8 caracteres
b. Contém pelo menos 1 maiúscula, 1 minúscula, 1 número e 1 dos seguintes
símbolos: !@#$%
'''
senha = input("Digite a senha: ")

def validar_senha(senha):

    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_simbolo = False
    simbolos_validos = "!@#$%"

    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in simbolos_validos:
            tem_simbolo = True

    return tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo

validar_senha(senha) 

if validar_senha(senha):
    print("Senha válida")
else:
    print("Senha inválida")