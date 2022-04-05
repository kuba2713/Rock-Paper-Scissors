import random

# Funciones

def preguntar_p1():
    while True:
        player1 = input("Player One choose rock(1), paper(2) or scissors(3): ")
        if player1 == "rock":
            player1 = 1
        elif player1 == "paper":
            player1 = 2
        elif player1 == "scissors":
            player1 = 3
        else:
            player1 = int(player1)

        if player1 in range(1,4):
            break

    return player1

def preguntar_p2():
    while True:
        player2 = input("Player Two choose rock(1), paper(2) or scissors(3): ")
        if player2 == "rock":
            player2 = 1
        elif player2 == "paper":
            player2 = 2
        elif player2 == "scissors":
            player2 = 3
        else:
            player2 = int(player2)

        if player2 in range(1,4):
            break

    return player2

def generar_radom():
    numeroaleatorio = random.randint(1, 3)
    print("CPU chose " + str(numeroaleatorio))
    return numeroaleatorio

#---------------------------------------------------------------------------------
# Programa en sí

while True:
    playmode = input("Choose Versus Mode(1) or CPU Mode(2): ")
    if int(playmode) == 1:
      player1 = preguntar_p1()
      player2 = preguntar_p2()
    if int(playmode) == 2:
      player1 = preguntar_p1()
      player2 = generar_radom()
    else:
      print("Error. Wrong mode.")

    #---------------------------------------------------------------------------------
    # Reglas

    if player1 == player2:
        print("Tie!")
    elif player1 == 1 and player2 == 2:
        print("Player Two win!")
    elif player1 == 1 and player2 == 3:
        print("Player One win!")
    elif player1 == 2 and player2 == 1:
        print("Player One win!")
    elif player1 == 2 and player2 == 3:
        print("Player One win!")
    elif player1 == 3 and player2 == 2:
        print("Player One win!")
    elif player1 == 3 and player2 == 1:
        print("Player Two win!")
