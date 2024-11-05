import animate

def jogar(word):
    print(animate.stage1)

    letras_contida = []
    letras_digitadas = []
    tentativa = 6
    CHECK = True
    save_word = {i for i in word} 

    while CHECK:

        letra = str(input('Digite a letra: ')).lower()[0]

        if letra in save_word:
            save_word.remove(letra)
        
        if letra in letras_digitadas:
            print(f'\033[33mA letra "{letra}" já foi digitada!\033[0m')
        elif letra in word:
            letras_contida.append(letra)
        else:
            print(f'A letra "{letra}" não está contida na palavra!')
            tentativa -= 1

        for i in word:
            if i in letras_contida:
                print(i, end='')
            else:
                print('_', end='')

        print()
        letras_digitadas.append(letra)

        if tentativa == 6:
            print(animate.stage1)
        elif tentativa == 5:
            print(animate.stage2)
        elif tentativa == 4:
            print(animate.stage3)
        elif tentativa == 3:
            print(animate.stage4)
        elif tentativa == 2:
            print(animate.stage5)
        elif tentativa == 1:
            print(animate.stage6)
        else:
            print(animate.stage7)
            print(f'A palavra era {word}')
            print('VOCÊ PERDEU!!!')
            break

        if len(save_word) == 0:
            print('VOCÊ GANHOU!!!')
            break

        exibir_palavra = ' '.join(letras_digitadas)
        print(f'Letras digitadas: {exibir_palavra}')