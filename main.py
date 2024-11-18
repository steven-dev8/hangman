import tkinter as tk
from tkinter import messagebox
import random

# Listas de palavras do jogo
fruit_word = [
    'abacate', 'acerola', 'banana', 'maca', 'laranja', 'melancia', 'manga', 'uva', 'pera', 'abacaxi', 
    'caju', 'coco', 'framboesa', 'groselha', 'limao', 'maracuja', 'marmelo', 'melao', 'kiwi', 'pessego', 
    'ameixa', 'cabeludinha', 'damasco', 'figo', 'jabuticaba', 'jaca', 'pitangas', 'tangerina', 'tamarindo', 
    'fruta-do-conde', 'acai', 'cranberry', 'physalis', 'tamarillo', 'pera-dagua', 'pinha', 'ameixa-preta', 
    'melancia-amarela', 'fruta-pao', 'murici', 'pequi', 'bacuri', 'guarana', 'bergamota'
]
# palavras com separadores tipo / ou - foram consideradas todas como com hífen
ti_word = [
    'hardware', 'software', 'sistema operacional', 'rede', 'servidor', 'banco de dados', 'firewall', 
    'antivírus', 'cloud computing', 'virtualização', 'api', 'algoritmo', 'programação', 'desenvolvimento', 
    'frontend', 'backend', 'fullstack', 'devops', 'inteligência-artificial', 'machine learning', 'big-data', 
    'data science', 'devsecops', 'containerização', 'microserviços', 'ci-cd', 'linux', 'windows', 'macos', 
    'android', 'ios', 'internet das coisas', 'blockchain', 'cibersegurança', 'ux-ui', 'iot', 'framework', 
    'biblioteca', 'repositório', 'versionamento', 'git', 'html', 'css', 'javascript', 'python', 'java', 
    'c', 'sql', 'nosql', 'scripting'
]

class HangmanGame:
    def __init__(self, root, word_list):
        self.root = root
        self.root.title("Jogo da Forca")
        self.word = random.choice(word_list)
        
        # Adicionar todos os hífens presentes na palavra aos palpites iniciais
        self.guesses = ''.join([char for char in self.word if char == '-'])
        self.errors = 0
        self.game_over = False  # Flag para controlar o estado do jogo

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.word_label = tk.Label(self.root, text="", font=("Arial", 18))
        self.word_label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack()
        self.entry.bind('<Return>', self.check_guess)

        self.guesses_label = tk.Label(self.root, text="Palpites: ", font=("Arial", 14))
        self.guesses_label.pack(pady=10)

        self.update_word_label()
        self.draw_hangman()

    def check_guess(self, event):
        if self.game_over:
            return  # Ignorar palpites se o jogo terminou

        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        
        # Validar entrada: apenas uma letra e alfabética
        if not guess.isalpha() or len(guess) != 1:
            return
        
        if guess in self.guesses:
            return
        
        self.guesses += guess

        print(f"Palpites atuais: {self.guesses}")  # Depuração
        print(f"Palavra: {self.word}")            # Depuração

        if guess in self.word:
            self.update_word_label()
            if self.check_win():
                self.game_over = True
                self.entry.config(state='disabled')  # Desabilitar entrada
                self.root.lift()  # Trazer a janela do jogo para frente
                messagebox.showinfo("Parabéns!", "Você acertou a palavra!", parent=self.root)
                self.ask_play_again()
        else:
            self.errors += 1
            self.draw_hangman()
            if self.errors > 5:
                self.game_over = True
                self.entry.config(state='disabled')  # Desabilitar entrada
                self.root.lift()  # Trazer a janela do jogo para frente
                messagebox.showinfo("Fim de Jogo", f"Você perdeu! A palavra era: {self.word}", parent=self.root)
                self.ask_play_again()

        self.update_guesses_label()

    def update_word_label(self):
        display_word = ''
        for letter in self.word:
            if letter in self.guesses or letter == '-':
                display_word += letter + ' '
            else:
                display_word += '_ '
        self.word_label.config(text=display_word)

    def update_guesses_label(self):
        # Adicionar um espaço entre cada letra
        spaced_guesses = ' '.join(self.guesses)
        try:
            self.guesses_label.config(text=f"Palpites: {spaced_guesses}")
        except tk.TclError:
            # A janela pode ter sido fechada, então ignorar
            pass

    def draw_hangman(self):
        self.canvas.delete("all")
        # Base do forca
        self.canvas.create_line(50, 350, 150, 350, width=2)
        self.canvas.create_line(100, 350, 100, 50, width=2)
        self.canvas.create_line(100, 50, 250, 50, width=2)
        self.canvas.create_line(250, 50, 250, 100, width=2)

        # Desenhar partes do boneco conforme o número de erros
        if self.errors > 0:
            # Cabeça
            self.canvas.create_oval(225, 100, 275, 150, width=2)
        if self.errors > 1:
            # Corpo
            self.canvas.create_line(250, 150, 250, 250, width=2)
        if self.errors > 2:
            # Braço esquerdo
            self.canvas.create_line(250, 180, 200, 220, width=2)
        if self.errors > 3:
            # Braço direito
            self.canvas.create_line(250, 180, 300, 220, width=2)
        if self.errors > 4:
            # Perna esquerda
            self.canvas.create_line(250, 250, 200, 300, width=2)
        if self.errors > 5:
            # Perna direita
            self.canvas.create_line(250, 250, 300, 300, width=2)

    def check_win(self):
        for letter in self.word:
            if letter not in self.guesses and letter != '-':
                return False
        return True

    def ask_play_again(self):
        answer = messagebox.askyesno("Jogar Novamente", "Deseja jogar novamente?", parent=self.root)
        if answer:
            self.restart_game()
        else:
            self.root.destroy()

    def restart_game(self):
        self.word = random.choice(fruit_word + ti_word)
        # Reiniciar os palpites com todos os hífens presentes na nova palavra
        self.guesses = ''.join([char for char in self.word if char == '-'])
        self.errors = 0
        self.game_over = False
        self.entry.config(state='normal')  # Reabilitar entrada
        self.update_word_label()
        self.update_guesses_label()
        self.draw_hangman()

if __name__ == "__main__":
    root = tk.Tk()
    word_list = fruit_word + ti_word
    game = HangmanGame(root, word_list)
    root.mainloop()