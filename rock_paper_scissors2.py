import random

# Listado caracteres especiales

lista = ['@','"','#','·','~','$','%','&','¬','/','(',')',"'",'?','¿','¡','`','^','[','+','*',']','¨','´','{','}',',',';','.',':','•','·','-','_','<','>']
numeros = ['0','1','2','3','4','5','6','7','8','9']

# Funciones

def preguntar_p1():
    invalido = False
    while True:
        player1 = input("Player One choose rock(1), paper(2) or scissors(3): ")
        for i in lista:
            if player1.__contains__(i): 
                invalido = True
                break
            else:
                continue       
        if player1.__contains__('½'):
            print('Invalid input, try again')
            continue
        elif player1.isalpha():
            for y in numeros:
                if player1.__contains__(y):
                    invalido = True
                    continue
            if invalido == True:
                print('Invalid input, try again')
            elif player1 == "rock":
                player1 = 1
                return player1
            elif player1 == "paper":
                player1 = 2
                return player1
            elif player1 == "scissors":
                player1 = 3
                return player1
            else:
                print('Invalid input, try again')

        elif player1.isnumeric():
            player1 = int(player1)
            if player1 == 0:
                print('Invalid input, try again')
            elif player1 > 3:
                print('Invalid input, try again')
            else:
                return player1
        else:
            print('Invalid input, try again')

def preguntar_p2():
    invalido = False
    while True:
        player2 = input("Player Two choose rock(1), paper(2) or scissors(3): ")
        for i in lista:
            if player2.__contains__(i): 
                invalido = True
                break
            else:
                continue       
        if player2.__contains__('½'):
            print('Invalid input, try again')
            continue
        elif player2.isalpha():
            for y in numeros:
                if player2.__contains__(y):
                    invalido = True
                    continue
            if invalido == True:
                print('Invalid input, try again')
            elif player2 == "rock":
                player2 = 1
                return player2
            elif player2 == "paper":
                player2 = 2
                return player2
            elif player2 == "scissors":
                player2 = 3
                return player2
            else:
                print('Invalid input, try again')

        elif player2.isnumeric():
            player2 = int(player2)
            if player2 == 0:
                print('Invalid input, try again')
            elif player2 > 3:
                print('Invalid input, try again')
            else:
                return player2
        else:
            print('Invalid input, try again')

def generar_radom():
    numeroaleatorio = random.randint(1, 3)
    print("CPU chose " + str(numeroaleatorio))
    return numeroaleatorio

#---------------------------------------------------------------------------------
# Programa en sí

while True:
    bucleplaymode = True
    while bucleplaymode == True:
        playmode = input("Choose Versus Mode(1) or CPU Mode(2): \n(Type x to exit the program)")
        if playmode == 'x':
            exit()
        elif playmode.isnumeric():
            if playmode.__contains__('½'):
                print('Invalid input, try again')
                continue
            elif int(playmode) == 1:
                bucleplaymode = False                
                player1 = preguntar_p1()
                player2 = preguntar_p2()
            elif int(playmode) == 2:
                bucleplaymode = False 
                player1 = preguntar_p1()
                player2 = generar_radom()
            else:
                print('Invalid input, try again')
        else:
            print('\nWrong input, try again\n')

    #---------------------------------------------------------------------------------
    # Reglas

    if player1 == player2:
        print("Tie!")
        bucleplaymode = False     
    elif player1 == 1 and player2 == 2:
        print("Player Two win!")
        bucleplaymode = False     
    elif player1 == 1 and player2 == 3:
        print("Player One win!")
        bucleplaymode = False     
    elif player1 == 2 and player2 == 1:
        print("Player One win!")
        bucleplaymode = False     
    elif player1 == 2 and player2 == 3:
        print("Player One win!")
        bucleplaymode = False     
    elif player1 == 3 and player2 == 2:
        print("Player One win!")
        bucleplaymode = False     
    elif player1 == 3 and player2 == 1:
        print("Player Two win!")
        bucleplaymode = False     
