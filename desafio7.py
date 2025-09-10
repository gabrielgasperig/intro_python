'''
Receba idade, renda mensal e dívidas. Classifique risco:
a. Alta: renda < 2000 e dívidas > 50% da renda
b. Média: renda 2000–5000 ou dívidas 30–50%
c. Baixa: renda > 5000 e dívidas < 30%
d. Outros casos: médio-baixo
'''

def classificacao_risco(idade, renda, dividas):
    idade = int(input("Digite a sua idade: "))
    while idade <= 0:
        idade = int(input("Digite idade valida: "))

    renda = float(input("Digite a sua renda mensal: R$"))
    while renda < 0:
        renda = int(input("Digite renda valida: R$"))

    dividas = float(input("Digite o seu debito em aberto: R$"))
    while renda < 0:
        dividas = int(input("Digite debito valido: R$"))

    if renda < 2000 and dividas > renda * 0.5:
        print("Classificacao de risco alta.")
    elif renda >= 2000 and renda <= 5000 and dividas >= 0.3 * renda and dividas <= 0.5 * renda:
        print("Classificacao de risco media.")
    elif renda > 5000 and dividas < 0.3 * renda:
        print("Classificacao de risco baixa.")
    else:
        print("Classificacao de risco media-baixa.")
        
classificacao_risco(0, 0, 0)