def select():
    while True:
        menu = input('''\033[32m
██   ██ ██    ██ ███    ██  ██████  ███    ███  █████  ███    ██ 
██   ██ ██    ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
███████ ██    ██ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
██   ██ ██    ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
██   ██  ██████  ██   ████  ██████  ██      ██ ██   ██ ██   ████
                                          \033[0mCreated by \033[33m@Stevendev8\033[0m
                     
               #CLASSES
1 - FRUTAS
2 - TI
SELECIONE A CLASSE DAS PALAVRAS: ''')
        if menu in ['1', '2']:
            return int(menu)
        else:
            print('\033[31mSELECIONE UMA OPÇÃO VÁLIDA\033[0m')

def cycle():
    while True:
        select = input('DESEJA JOGAR NOVAMENTE? [S/N]: ').upper()[0]
        if select in ['S', 'N']:
            return select
        else:
            print('\033[31mSELECIONE UMA OPÇÃO VÁLIDA\033[0m')