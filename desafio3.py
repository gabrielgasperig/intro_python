'''
Leia peso e altura, calcule o IMC e classifique:
a. <18.5: abaixo do peso
b. 18.5–24.9: peso normal
c. 25–29.9: sobrepeso
d. 30–34.9: obesidade grau I
e. 35–39.9: obesidade grau II
f. ≥40: obesidade grau III
'''
def calcular_imc(peso, altura):
    peso = float(input('Digite seu peso em kg: '))
    altura = float(input('Digite sua altura em metros: '))
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print(f'Seu IMC e {imc:.2f}, voce esta abaixo do peso')
    elif 18.5 <= imc <= 24.9:
        print(f'Seu IMC e {imc:.2f}, voce esta com peso normal')
    elif 25 <= imc <= 29.9:
        print(f'Seu IMC e {imc:.2f}, voce esta com sobrepeso')
    elif 30 <= imc <= 34.9:
        print(f'Seu IMC e {imc:.2f}, voce esta com obesidade grau I')
    elif 35 <= imc <= 39.9:
        print(f'Seu IMC e {imc:.2f}, voce esta com obesidade grau II')
    else:
        print(f'Seu IMC e {imc:.2f}, voce esta com obesidade grau III')
    return imc

calcular_imc(0, 0)