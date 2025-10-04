# Importa as funções de execução de cada arquivo de desafio
from desafio_01 import executar_desafio_01
from desafio_02 import executar_desafio_02
from desafio_03 import executar_desafio_03
from desafio_04 import executar_desafio_04
from desafio_05 import executar_desafio_05
from desafio_06 import executar_desafio_06
from desafio_07 import executar_desafio_07
from desafio_08 import executar_desafio_08
from desafio_09 import executar_desafio_09
from desafio_10 import executar_desafio_10

# Importa a função utilitária para obter a escolha do usuário
from utils import obter_int_no_intervalo

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n" + "="*40)
    print(" " * 10 + "MENU DE DESAFIOS PYTHON")
    print("="*40)
    print("1. Cálculo de Bônus de Funcionário")
    print("2. Classificação de Triângulos")
    print("3. Cálculo e Classificação de IMC")
    print("4. Boletim Escolar (Média e Situação)")
    print("5. Validador de Datas")
    print("6. Verificação de Voto")
    print("7. Classificação de Risco Financeiro")
    print("8. Jogo de Pontuação com Cartas")
    print("9. Calculadora de Descontos")
    print("10. Validador de Senha Segura")
    print("0. Sair do programa")
    print("="*40)

def main():
    """Função principal que gerencia a execução dos desafios."""
    
    # Um dicionário que mapeia a escolha do usuário à função correspondente
    desafios = {
        1: executar_desafio_01,
        2: executar_desafio_02,
        3: executar_desafio_03,
        4: executar_desafio_04,
        5: executar_desafio_05,
        6: executar_desafio_06,
        7: executar_desafio_07,
        8: executar_desafio_08,
        9: executar_desafio_09,
        10: executar_desafio_10,
    }
    
    while True:
        exibir_menu()
        
        # Usa a função utilitária para obter uma escolha válida
        escolha = obter_int_no_intervalo(
            "Escolha um desafio para executar: ", 0, 10
        )
        
        if escolha == 0:
            print("Encerrando o programa. Até a próxima!")
            break
            
        # Pega a função correspondente no dicionário
        funcao_a_executar = desafios.get(escolha)
        
        # Executa a função
        if funcao_a_executar:
            funcao_a_executar()
            input("\nPressione Enter para voltar ao menu...")
            
if __name__ == "__main__":
    main()