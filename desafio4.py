'''
Leia a nota final de três provas (0 a 10). Calcule a média e informe:
a. Média ≥ 7: aprovado
b. Média ≥ 5 e <7: recuperação
c. Média <5: reprovado
d. Se alguma nota for 0: reprovado automático
'''

def boletim(nota1, nota2, nota3):
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    media = (nota1 + nota2 + nota3) / 3
    
    if nota1 <= 0 or nota2 <= 0 or nota3 <= 0:
        print("Voce foi reprovado. Estude mais!")
    elif nota1 > 10 or nota2 > 10 or nota3 > 10:
        print("Digite notas validas")
    elif media >= 7:
        print("Parabens voce foi aprovado!")
    elif media >= 5 and media < 7:
        print("Voce esta em recuperação") 
    else:
        print("Voce foi reprovado. Estude mais!")
    return media

boletim(0, 0, 0)