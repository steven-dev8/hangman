import menu, functions, random

fruit_word = ["Abacate", "Acerola", "Banana", "Maca", "Laranja", "Melancia", "Manga", "Uva", "Pera", "Abacaxi", "Caju", "Coco", "Framboesa", "Groselha", "Limao", "Maracuja", "Marmelo", "Melao", "Kiwi", "Pessego", "Ameixa", "Cabeludinha", "Damasco", "Figo", "Jabuticaba", "Jaca", "Pitangas", "Tangerina", "Tamarindo", "Fruta-do-conde", "Acai", "Cranberry", "Physalis", "Tamarillo", "Pera-dagua", "Pinha", "Ameixa-preta", "Melancia-amarela", "Fruta-pao", "Murici", "Pequi", "Bacuri", "Guarana", "Bergamota"]

ti_word = ["Hardware", "Software", "Sistema operacional", "Rede", "Servidor", "Banco de dados", "Firewall", "Antivírus", "Cloud computing", "Virtualização", "API", "Algoritmo", "Programação", "Desenvolvimento", "Frontend", "Backend", "Fullstack", "DevOps", "Inteligência artificial", "Machine learning", "Big data", "Data science", "DevSecOps", "Containerização", "Microserviços", "CI/CD", "Linux", "Windows", "macOS", "Android", "iOS", "Internet das coisas", "Blockchain", "Cibersegurança", "UX/UI", "IoT", "Framework", "Biblioteca", "Repositório", "Versionamento", "Git", "HTML", "CSS", "JavaScript", "Python", "Java", "C++", "SQL", "NoSQL", "Scripting"]


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