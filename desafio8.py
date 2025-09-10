'''
Dado a sequência 'B', 'C', 'D', 'A' para as 4 cartas (A, B, C, D), o usuário escolhe a
sequência de 4 cartas e recebe uma pontuação baseada nas seguintes regras:
a. Resposta correta: 10 pontos para cada acerto
b. Resposta A: bônus 5 pontos independente de estar certo
c. Resposta C seguida de D na sequência: bônus extra 5 pontos independente
de estar certo
d. Sistema exibe a pontuação do usuário.

Obs: Pontuação máxima = 50.
'''

def calcular_pontos(resposta):
    sequencia = ['B', 'C', 'D', 'A']
    pontos = 0
    resposta = []

    for i in range(4):
        carta = input(f'Digite a carta da posição {i + 1}: ').upper()
        resposta.append(carta[0])

    for i in range(4):
        if resposta[i] == sequencia[i]:
            pontos += 10
        
        if resposta[i] == 'A':
            pontos += 5
        
        if resposta[i] == 'C' and resposta[i + 1] == 'D':
            pontos += 5

    if pontos > 50:
        pontos = 50
    
    print(f'Pontuacao final: {pontos}')
      
calcular_pontos(0)