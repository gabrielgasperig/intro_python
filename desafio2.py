'''
Receba três lados e informe se formam um triângulo. Classifique como: equilátero,
isósceles ou escaleno.
'''

def classifica_triangulo(lado1, lado2, lado3):
    lado1 = float(input('Digite o comprimento do lado 1: '))
    lado2 = float(input('Digite o comprimento do lado 2: '))    
    lado3 = float(input('Digite o comprimento do lado 3: '))
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        print("Digite valores validos")
    elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        print("Nao forma um triangulo")
    elif lado1 == lado2 == lado3:
        print("O triangulo e Equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("O triangulo e Isosceles")
    else:
        print("O triangulo e Escaleno")
    
classifica_triangulo(0, 0, 0)