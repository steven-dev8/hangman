# Hangman🎮

Este script é um jogo da forca (Hangman) projetado para ser divertido e desafiador. O jogador deve adivinhar uma palavra secreta, letra por letra, antes que o número máximo de tentativas seja alcançado. O jogo inclui uma interface simples e interativa.

## Características:

- **Jogo Clássico:** Uma implementação do tradicional jogo da forca, onde o jogador adivinha letras para revelar uma palavra secreta.
- **Interface de Texto:** Um menu simples e intuitivo que orienta o usuário durante o jogo.
- **Palavras Aleatórias:** O jogo seleciona palavras aleatórias de uma lista predefinida, garantindo uma experiência variada a cada partida.
- **Número de Tentativas:** O jogador tem um número limitado de tentativas para adivinhar a palavra, aumentando o desafio.
- **Feedback Instantâneo:** O jogo fornece feedback imediato sobre as letras adivinhadas, mostrando quais estão corretas e quais não estão.

## Como Funciona:

1. O jogo inicia e apresenta uma palavra oculta representada por traços.
2. O jogador deve adivinhar uma letra.
3. Se a letra estiver na palavra, ela será revelada. Caso contrário, o jogador perde uma tentativa.
4. O jogo continua até que a palavra seja adivinhada ou que as tentativas se esgotem.

## Guia de Execução

### Requisitos

- Python 3 instalado.

### Instruções para Usuários Windows

1. Execute o arquivo `hangman.bat`.

### Instruções para Usuários Linux

1. Abra uma IDE compatível com Python ou o terminal (BASH).
2. Localize o arquivo `main.py`.
3. No terminal, execute o seguinte comando:

   ```bash
   python3 main.py
