# Hangman

Este é um jogo da forca desenvolvido em Python, onde o jogador deve adivinhar uma palavra secreta letra por letra. O projeto é simples e focado em aprendizado, ideal para quem está começando a programar.

---

## 🖼️ Imagens do Jogo

### Menu do Jogo
![Menu do Jogo](/assets/menu.png)

### Janela do Jogo
![Janela do Jogo](/assets/gamewindow.png)

---

## 📝 Funcionalidades

- Exibe um painel de letras e espaços em branco para a palavra secreta.
- Permite que o jogador insira uma letra por tentativa.
- Verifica automaticamente se a letra está na palavra secreta.
- Atualiza o painel conforme o progresso do jogador.
- Limita o número de tentativas erradas antes de finalizar o jogo.

---

## 🚀 Como executar o código

### Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina. Este projeto foi testado com Python 3.x.
---

## 🛠️ Dependências

Este projeto utiliza o `tkinter` para a interface gráfica. O `tkinter` geralmente já vem pré-instalado com o Python. No entanto, caso você encontre um erro relacionado ao `tkinter`, siga as instruções abaixo para instalá-lo:

### No Ubuntu/Debian:
```bash
sudo apt-get install python3-tk
```

### Passos
1. Clone este repositório:
   ```bash
   git clone https://github.com/steven-dev8/hangman
   cd hangman
   ```

2. Execute o arquivo principal:
   ```bash
   python menu.py
   ```

3. Siga as instruções exibidas no menu da janela que abre para jogar.

---

## 🎮 Como jogar

1. O jogo selecionará aleatoriamente uma palavra secreta.
2. Você deverá digitar uma letra por tentativa.
3. Caso acerte, a letra será revelada na posição correta.
4. Caso erre, perderá uma tentativa. O jogo exibirá quantas tentativas você ainda tem.
5. O jogo termina quando:
   - Você adivinha a palavra inteira (Vitória 🎉).
   - Suas tentativas acabam (Derrota 💀).

---
**Divirta-se jogando Hangman e explorando o código!**
