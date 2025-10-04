
# 🚀 Desafios - Introdução à Programação em Python

Repositório criado para entrega do **Trabalho M1** da disciplina **Introdução à Programação em Python** (UNIVALI).

O projeto consiste na resolução de 10 desafios de lógica, que foram posteriormente refatorados para formar uma aplicação interativa e modular, seguindo boas práticas de desenvolvimento de software.

## 🎯 Objetivo

O objetivo deste trabalho foi evoluir da simples implementação de algoritmos para a criação de um projeto mais robusto e organizado, focando em:

  * Praticar lógica de programação, estruturas condicionais e manipulação de dados em Python.
  * Aplicar boas práticas de código, como **Separação de Responsabilidades (SoC)** e **DRY (Don't Repeat Yourself)**.
  * Estruturar um projeto com múltiplos arquivos, separando a lógica de negócio, as funções utilitárias e o ponto de entrada da aplicação.
  * Documentar o código de forma clara utilizando **Docstrings** e **Type Hints**.
  * Criar uma interface de linha de comando (CLI) interativa para o usuário.

## ✨ Funcionalidades e Boas Práticas

  * 📁 **Modularidade:** Cada desafio está contido em seu próprio arquivo (`desafio_XX.py`), facilitando a manutenção e a organização.
  * ♻️ **Reutilização de Código:** Funções comuns, como a captura e validação de dados do usuário, foram centralizadas no arquivo `utils.py`.
  * 🧩 **Separação de Responsabilidades:** A lógica de negócio (cálculos) foi isolada da lógica de interface (funções de `input` e `print`), tornando o código mais limpo e testável.

## 💻 Desafios Incluídos

1.  **Cálculo de Bônus de Funcionário**
2.  **Classificação de Triângulos**
3.  **Cálculo e Classificação de IMC**
4.  **Boletim Escolar**
5.  **Validador de Datas**
6.  **Verificação de Voto**
7.  **Classificação de Risco Financeiro**
8.  **Jogo de Pontuação com Cartas**
9.  **Calculadora de Descontos**
10. **Validador de Senha Segura**

## 📂 Estrutura de Arquivos

```
/
│
├── main.py             # Ponto de entrada principal, exibe o menu interativo
├── utils.py            # Funções utilitárias reutilizáveis
│
├── desafio_01.py       # Solução do Desafio 1
├── desafio_02.py       # Solução do Desafio 2
├── desafio_03.py       # Solução do Desafio 3
├── desafio_04.py       # Solução do Desafio 4
├── desafio_05.py       # Solução do Desafio 5
├── desafio_06.py       # Solução do Desafio 6
├── desafio_07.py       # Solução do Desafio 7
├── desafio_08.py       # Solução do Desafio 8
├── desafio_09.py       # Solução do Desafio 9
└── desafio_10.py       # Solução do Desafio 10
```

## ▶️ Como Executar

#### 🐍 Pré-requisitos

  * É necessário ter o **Python 3.x** instalado.

#### ⚙️ Passos

1.  Garanta que todos os 12 arquivos `.py` estejam na mesma pasta.

2.  Abra um terminal (ou Prompt de Comando) e navegue até o diretório do projeto.

3.  Execute o programa principal com o comando:

    ```bash
    python main.py
    ```

    *(ou `python3 main.py` em alguns sistemas)*

4.  Navegue pelo menu interativo para escolher qual desafio executar.