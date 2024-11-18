import tkinter as tk
from tkinter import messagebox
import main  # Certifique-se de que main.py está no mesmo diretório
import time
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s - %(levelname)s - %(message)s')

class MenuApp:
    def __init__(self, root):
        start_time = time.time()
        logging.debug("Iniciando MenuApp")
        
        self.root = root
        self.root.title("Jogo da Forca - Menu")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Pré-carregar fontes
        self.root.option_add('*Font', 'Courier 10')

        self.create_widgets()
        
        end_time = time.time()
        logging.debug(f"MenuApp inicializado em {end_time - start_time:.2f} segundos")

    def create_widgets(self):
        start_time = time.time()
        logging.debug("Criando widgets")
        
        # Título com arte ASCII simplificada
        title = """
        ██   ██ ██    ██ ███    ██  ██████  ███    ███  █████  ███    ██ 
        ██   ██ ██    ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
        ███████ ██    ██ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
        ██   ██ ██    ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
       ██   ██  ██████  ██   ████  ██████  ██      ██ ██   ██ ██   ████
        Created by @Stevendev8
        """
        self.title_label = tk.Label(self.root, text=title, font=("Courier", 10), fg="green", justify="center")
        self.title_label.pack(pady=20)

        # Opções de classe de palavras
        self.option_frame = tk.Frame(self.root)
        self.option_frame.pack(pady=10)

        self.create_buttons()
        
        end_time = time.time()
        logging.debug(f"Widgets criados em {end_time - start_time:.2f} segundos")

    def create_buttons(self):
        buttons = [
            ("1 - FRUTAS", self.select_fruits),
            ("2 - TI", self.select_ti)
        ]
        
        for text, command in buttons:
            tk.Button(
                self.option_frame,
                text=text,
                font=("Courier", 14),
                width=20,
                command=command
            ).pack(pady=10)

    def select_fruits(self):
        self.start_game(main.fruit_word)

    def select_ti(self):
        self.start_game(main.ti_word)

    def start_game(self, word_list):
        self.root.withdraw()  # Esconder o menu
        game_window = tk.Toplevel()
        game = main.HangmanGame(game_window, word_list)
        game_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        if messagebox.askokcancel("Sair", "Deseja sair do jogo?"):
            self.root.destroy()

def ask_play_again():
    answer = messagebox.askquestion("Jogar Novamente", "Deseja jogar novamente?")
    return answer == 'yes'

def main_menu():
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()

if __name__ == "__main__":
    main_menu()