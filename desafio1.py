'''
Peça o salário do funcionário e o tempo de empresa. Calcule o bônus
considerando as seguintes regras:
a. Salário < 2000 e tempo ≥ 5 anos: bônus de 20%
b. Salário < 2000 e tempo < 5 anos: bônus de 10%
c. Salário ≥ 2000 e tempo ≥ 5 anos: bônus de 5%
d. Salário ≥ 2000 e tempo < 5 anos: sem bônus
'''

def calcular_bonus(salario, tempo_empresa):
    salario = float(input('Digite seu salario: '))
    tempo_empresa = int(input('Digite o tempo de empresa: '))
    
    if salario < 2000 and tempo_empresa >= 5:
        bonus = salario * 0.20
        print(f'Voce recebeu um bonus de {bonus}')
    elif salario < 2000 and tempo_empresa < 5:
        bonus = salario * 0.10
        print(f'Voce recebeu um bonus de {bonus}')
    elif salario >= 2000 and tempo_empresa >= 5:
        bonus = salario * 0.05
        print(f'Voce recebeu um bonus de {bonus}')
    elif salario >= 2000 and tempo_empresa < 5:
        bonus = 0
        print('Voce nao tem direito a bonus')
    return bonus

calcular_bonus(0, 0)