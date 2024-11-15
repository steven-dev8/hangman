import menu, functions, random

fruit_word = ['abacate', 'acerola', 'banana', 'maca', 'laranja', 'melancia', 'manga', 'uva', 'pera', 'abacaxi', 
 'caju', 'coco', 'framboesa', 'groselha', 'limao', 'maracuja', 'marmelo', 'melao', 'kiwi', 'pessego', 
 'ameixa', 'cabeludinha', 'damasco', 'figo', 'jabuticaba', 'jaca', 'pitangas', 'tangerina', 'tamarindo', 
 'fruta-do-conde', 'acai', 'cranberry', 'physalis', 'tamarillo', 'pera-dagua', 'pinha', 'ameixa-preta', 
 'melancia-amarela', 'fruta-pao', 'murici', 'pequi', 'bacuri', 'guarana', 'bergamota']


ti_word = ['hardware', 'software', 'sistema operacional', 'rede', 'servidor', 'banco de dados', 'firewall', 
 'antivírus', 'cloud computing', 'virtualização', 'api', 'algoritmo', 'programação', 'desenvolvimento', 
 'frontend', 'backend', 'fullstack', 'devops', 'inteligência artificial', 'machine learning', 'big data', 
 'data science', 'devsecops', 'containerização', 'microserviços', 'ci/cd', 'linux', 'windows', 'macos', 
 'android', 'ios', 'internet das coisas', 'blockchain', 'cibersegurança', 'ux/ui', 'iot', 'framework', 
 'biblioteca', 'repositório', 'versionamento', 'git', 'html', 'css', 'javascript', 'python', 'java', 
 'c++', 'sql', 'nosql', 'scripting']

select = menu.select()

while True:
    if select == 1:
        random_number = random.randint(0, 4)
        random.shuffle(fruit_word)
        functions.jogar(fruit_word[random_number])
    elif select == 2:
        random_number = random.randint(0, 4)
        random.shuffle(ti_word)
        functions.jogar(ti_word[random_number])

    cycle = menu.cycle()
    if cycle == 'N':
        break

print('OBRIGADO POR JOGAR')