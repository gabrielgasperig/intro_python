'''
O usuário digita um preço de um produto e se ele é um cliente vip ou não e o
sistema exibe o preço do produto com desconto baseado nas seguintes regras:
a. Produto ≥ 100: desconto 20%
b. Produto ≥ 50 e <100: desconto 10%
c. Produto <50: sem desconto
d. Cliente VIP: +5% desconto adicional
'''

def calcular_desconto(preco, desconto, vip_ou_nao):
    preco = float(input("Digite o valor do produto: R$"))
    while preco <= 0:
        preco = float(input("Digite um valor valido: R$"))

    if preco >= 100:
        desconto = preco * 0.2
    elif preco >= 50 and preco < 100:
        desconto = preco * 0.1
    elif preco < 50:
        desconto = 0
    
    vip_ou_nao = int(input("Voce e cliente vip?\n1 - Sim\n0 - Nao\n"))
    while vip_ou_nao != 0 and vip_ou_nao != 1:
        vip_ou_nao = int(input("Digite resposta valida: "))

    if vip_ou_nao == 1:
        desconto += preco * 0.05

    valor_final = preco - desconto
    
    print(f'Desconto = R${desconto:.2f}\nValor final = R${valor_final:.2f}')
calcular_desconto(0, 0, 0)