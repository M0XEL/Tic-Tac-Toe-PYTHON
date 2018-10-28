
import os

player1_name = 'X'
player2_name = 'O'
current_player = player1_name
field = []
is_singleplayer = True
difficulty = 1

def printMainMenu():
    os.system('cls')
    print('_____MENU_____\n')
    print(' -1-  Start Round')
    print(' -2-  Open Settings')
    print(' -3-  Exit Game')

def printField():
    os.system('cls')
    print('_____ROUND_____\n')
    print(field[0] + '  ' + field[1] + '  ' + field[2])
    print(field[3] + '  ' + field[4] + '  ' + field[5])
    print(field[6] + '  ' + field[7] + '  ' + field[8])
    print('\n -0-  Exit Round')

def printSettingsMenu():
    os.system('cls')
    print('_____SETTINGS_____\n')

    if is_singleplayer: playmode = 'Singleplayer'
    else: playmode = 'Multiplayer'
    print(' -1-  Playmode: ' + playmode)

    if difficulty == 1: difficulty_str = 'Easy'
    elif difficulty == 2: difficulty_str = 'Medium'
    elif difficulty == 3: difficulty_str = 'Hard'
    else: difficulty_str = '[Unknown]'
    print(' -2-  Difficulty: ' + difficulty_str)

    print(' -3-  Return to Menu')

def getInput_numberCheck():
    input_key = input()
    if input_key.isdigit():
        return int(input_key)
    else:
        return -1

def togglePLayer():
    global current_player
    if current_player == player1_name:
        current_player = player2_name
    elif current_player == player2_name:
        current_player = player1_name

def togglePlaymode():
    global is_singleplayer
    if is_singleplayer: is_singleplayer = False
    else: is_singleplayer = True

def changeDifficulty():
    global difficulty
    if difficulty == 3: difficulty = 1
    else: difficulty += 1

def checkWin():

    # horizontally Win
    if (field[0] == current_player) and (field[1] == current_player) and (field[2] == current_player): return True
    elif field[3] == current_player and field[4] == current_player and field[5] == current_player: return True
    elif field[6] == current_player and field[7] == current_player and field[8] == current_player: return True

    # vertically Win
    elif field[0] == current_player and field[3] == current_player and field[6] == current_player: return True
    elif field[1] == current_player and field[4] == current_player and field[7] == current_player: return True
    elif field[2] == current_player and field[5] == current_player and field[8] == current_player: return True

    # diagonally Win
    elif field[0] == current_player and field[4] == current_player and field[8] == current_player: return True
    elif field[2] == current_player and field[4] == current_player and field[6] == current_player: return True

    else: return False

def startRound():

    global field
    for x in range(9):
        #field[x] = '-'
        field.append('-')

    printField()
    turn = 0
    is_playable = True
    loop = True
    while loop:      
        choice = getInput_numberCheck()
        if is_playable and choice > 0 and choice < 10:
            choice -= 1
            if field[choice] == '-':
                field[choice] = current_player
                turn += 1
                printField()
                if checkWin():
                    is_playable = False
                    print('Player ' + current_player + ' wins in Turn ' + str(turn))
                else: togglePLayer()
        elif choice == 0:
            loop = False

def openSettings():
    loop = True
    while loop:
        printSettingsMenu()
        choice = getInput_numberCheck()
        if choice == 1: togglePlaymode()
        elif choice == 2: changeDifficulty()
        elif choice == 3: loop = False
        else: print('Wrong Input!')


loop = True
while loop:
    printMainMenu()
    choice = getInput_numberCheck()
    if choice == 1: startRound()
    elif choice == 2: openSettings()
    elif choice == 3: loop = False
    else: print('Wrong Input!')