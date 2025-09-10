'''
Peça idade e nacionalidade. Informe se pode votar:
a. Apenas maiores de 18
b. Brasileiros: obrigatório, estrangeiros: opcional
c. Entre 16 e 17 anos: opcional
'''

def pode_votar(idade, nacionalidade):
    idade = int(input("Qual é a sua idade? "))
    while idade < 0:
        idade = int(input("Idade invalida, digite novamente: "))

    if idade < 16:
        print("Nao pode votar.")
        exit()

    nacionalidade = int(input("Selecione a sua nacionalidade:\n1 - Brasileiro\n2 - Estrangeiro\n"))
    while nacionalidade < 1 or nacionalidade > 2:
        nacionalidade = int(input("Nacionalidade invalida, digite novamente: "))

    if idade >= 16 and idade < 18:
        print("Pode votar opicionalmente.")
    elif idade >= 18 and nacionalidade == 1:
        print("Deve votar obrigatoriamente.")
    elif idade >= 16 and nacionalidade == 2:
        print("Pode votar opicionalmente.")
pode_votar(0, 0)