'''
Peça dia, mês e ano. Verifique se a data é válida (meses com 30 ou 31 dias,
fevereiro com 28/29).
'''

def data_valida():
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mês: '))
    ano = int(input('Digite o ano: '))

    if mes < 1 or mes > 12:
        print('Data inválida')
        return
    if dia < 1 or dia > 31:
        print('Data inválida')
        return
    if mes in [4, 6, 9, 11] and dia > 30:
        print('Data inválida')
        return
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia > 29:
                print('Data inválida')
                return
        elif dia > 28:
            print('Data inválida')
            return
    print('Data válida')

data_valida()