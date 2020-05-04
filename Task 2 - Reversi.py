#Adrian Price - 30588812
import copy

def new_board():
    newBoard =[]
    for i in range (0,8):
        if i == 3:
            newRow = [0,0,0,2,1,0,0,0]
        elif i == 4:
            newRow = [0,0,0,1,2,0,0,0]
        else:
            newRow = [0,0,0,0,0,0,0,0]
        newBoard.append(newRow)
    return newBoard

def score (currentBoard):
    s1 = 0
    s2 = 0
    for x in range (0,8):
        for y in range (0,8):
            if currentBoard[x][y] == 1:
                s1 += 1
            elif currentBoard[x][y] == 2:
                s2 += 1
    return s1, s2

def print_board (currentBoard):
    for x in range(0,8):
        rowDisplay = str(x + 1)
        for y in range (0,8):
            if (x,y) in valid_moves(currentBoard, currentPlayer):
                rowDisplay += "| * "
            else:
                if currentBoard[x][y] == 0:
                    rowDisplay += "|   "
                elif currentBoard[x][y] == 1:
                    rowDisplay += "| B "
                elif currentBoard[x][y] == 2:
                    rowDisplay += "| W "
        print(rowDisplay)
        print("  -------------------------------")
    print(" | a | b | c | d | e | f | g | h ")

def possibleDirections(posX, posY):
    totalPossibleDirections = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    validPossibleDirections = []

    for i in range (0,8):
        dirX = totalPossibleDirections[i][0]
        dirY = totalPossibleDirections[i][1]

        newPosX = posX + dirX
        newPosY = posY + dirY

        if (newPosX >= 0 and newPosY >= 0) and (newPosX < 8 and newPosY < 8):
            validPossibleDirections.append((dirX,dirY))

    return validPossibleDirections

def enclosing (board, player, pos, direct):
    i = pos[0] - 1
    j = pos[1] - 1
    dirX = direct[0]
    dirY = direct[1]
    if player == 1:
        otherPlayer = 2
    else:
        otherPlayer = 1

    while i < 7 and j < 7 and  i >= 1 and j >= 1:
        i += dirX
        j += dirY

        if board[i][j] == otherPlayer:
            if (i + dirX >= 0 and i + dirX < 8 and j + dirY >= 0 and j + dirY < 8):
                if board[i + dirX][j + dirY] == 0:
                    if (i + dirX >= 0 and i + dirX < 8 and i + dirY >= 0 and i + dirY < 8):
                        return True
                    else:
                        return False
        elif board[i][j] == player:
            return False
        elif board[i][j] == 0:
            return False

def valid_moves (board, player):
    validMoves  = []
    playerPositions = []
    for x in range (0,8):
        for y in range (0,8):
            if board[x][y] == player:
                playerPositions.append((x + 1, y + 1))
    amountPositions = len(playerPositions)
    for y in range (0, amountPositions):
        position = playerPositions[y]
        validPossibleDirections = possibleDirections(position[0],position[1])
        validDirection = []
        for x in range(0, len(validPossibleDirections)):
            if enclosing(board, player, position, validPossibleDirections[x]):
                validDirection.append(validPossibleDirections[x])

        for x in range (0, len(validDirection)):
            spaceValue = -1
            dirX = validDirection[x][0]
            dirY = validDirection[x][1]
            posX = position[0] - 1
            posY = position [1] - 1
            while spaceValue != 0 and True:
                posX += dirX
                posY += dirY
                if (posX <= 7 and posY <= 7) and ((posX >= 0 or posY >= 0)):
                    spaceValue = board[posX][posY]
                else:
                    break
            validMoves.append((posX,posY))
    return validMoves

def next_state(board, player, position):
    if player == 1:
        board[position[0]][position[1]] = 1
        nextPlayer = 2
    else:
        board[position[0]][position[1]] = 2
        nextPlayer = 1

    i = 0

    validPossibleDirections = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    while i < len(validPossibleDirections):
        posX = position[0]
        posY = position[1]

        validPossibleDirections = possibleDirections(posX, posY)

        dirX = validPossibleDirections[i][0]
        dirY = validPossibleDirections[i][1]

        posX += dirX
        posY += dirY

        while True and posX > 0 and posY > 0 and posX < 7 and posY < 7:
            while board[posX][posY] == nextPlayer and True and posX > 0 and posY > 0 and posX < 7 and posY < 7:
                posX = posX + dirX
                posY = posY + dirY
                if board[posX][posY] == player:
                    rightDirection = (dirX,dirY)
                elif board[posX][posY] == 0:
                    break
            if board[posX][posY] == 0:
                break
            elif posX >= 0 and posY >= 0 and posX < 8 and posY < 8:
                posX = posX + dirX
                posY = posY + dirY
            else:
                break
        i += 1
    posX = position[0] + rightDirection[0]
    posY = position[1] + rightDirection[1]
    while True:
        board[posX][posY] = player
        posX = posX + rightDirection[0]
        posY = posY + rightDirection[1]
        if board[posX][posY] == player:
            break
    return board, nextPlayer

def position(string):
    possibleLetters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range (0,8):
        if string[0] == possibleLetters[i]:
            posX = i
            break
        elif i == 7:
            return None
    if int(string[1]) > 0 and int(string[1]) <= 8:
        posY = int(string[1]) - 1
    else:
        return None

    return posY, posX

def reversePosition(position):
    possibleLetters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    posX = str(possibleLetters[position[1]])
    posY = str(position[0] + 1)

    return posX + posY

def run_two_players():
    global board
    board = new_board()
    global currentPlayer
    currentPlayer = 1
    gameOver = False
    specialCommands = ["score", "valid", "board", "end"]
    print("The game has begun. The game will finish when there are no avaliable moves left.")
    print("Type help for a list of commands. ")
    while True:
        print_board(board)
        userInput = input('\n' + "Player " + str(currentPlayer) + " please select a position to place a stone: ")
        while True:
            if userInput.lower() == "help":
                userInput = helpMenu()
            elif userInput.lower() in specialCommands:
                userInput = specialFunctions(userInput, board, currentPlayer)
            else:
                break
        if userInput.lower() == "quit":
            gameOver = True
            break
        valid = False
        while valid == False:
            if position(userInput) == None:
                userInput = input("Invalid position please try again: ")
            else:
                if position(userInput) not in valid_moves(board, currentPlayer):
                    userInput = input("This space is not a valid move for you, please try again: ")
                else:
                    valid = True
        nextState = next_state(board, currentPlayer, position(userInput))
        board = nextState [0]
        currentPlayer = nextState[1]
        if valid_moves(board, currentPlayer) == []:
            gameOver = True
            break

    if gameOver == True:
        playerOneScore = score(board)[0]
        playerTwoScore = score(board)[1]
        print("You have run out of moves to player so the game is over!")
        print("The final scores are, Player 1:", playerOneScore, " and Player 2", playerTwoScore)
        if playerOneScore > playerTwoScore:
            print("Player 1 wins!!!")
        elif playerTwoScore > playerOneScore:
            print("Player 2 wins!!!")
        else:
            print("The scores are equal, it is a draw.")

def run_single_player():
    global board
    board = new_board()
    global currentPlayer
    currentPlayer = 1
    specialCommands = ["score", "valid", "board", "end"]
    print('\n' + "The game has begun. You will be playing against an AI. The game will finish when there are no available moves left.")
    print("Type help for a list of commands. ")
    while True:
        if currentPlayer == 1:
            print_board(board)
            userInput = input('\n' + "Please select a position to place a stone: ")
            while True:
                if userInput.lower() == "help":
                    userInput = helpMenu()
                elif userInput.lower() in specialCommands:
                    userInput = specialFunctions(userInput, board, currentPlayer)
                else:
                    break
            if userInput.lower() == "quit":
                gameOver = True
                break
            valid = False
            while not valid:
                if position(userInput) == None:
                    userInput = input("Invalid position please try again: ")
                else:
                    if position(userInput) not in valid_moves(board, currentPlayer):
                        userInput = input("This space is not a valid move for you, please try again: ")
                    else:
                        valid = True
            print(position(userInput))
            nextState = next_state(board, currentPlayer, position(userInput))
            board = nextState[0]
            currentPlayer = nextState[1]
            if valid_moves(board, currentPlayer) == []:
                print("You have run out of moves to player so the game is over!")
                gameOver = True
                break
        else:
            currentScore = score(board)[1]
            testBoard = copy.deepcopy(board)
            moveList = valid_moves(testBoard, 2)
            bestScore = 0
            for i in range (len(moveList)):
                nextState = next_state(testBoard, currentPlayer, moveList[i])
                testBoard = nextState[0]
                newScore = score(testBoard)[1]
                if (newScore - currentScore) > bestScore:
                    bestScore = newScore - currentScore
                    bestMove = moveList[i]
                testBoard = copy.deepcopy(board)
            nextState = next_state(board, currentPlayer, bestMove)
            board = nextState[0]
            currentPlayer = nextState[1]
            print("The AI decided to place a stone on position", reversePosition(bestMove))

    if gameOver == True:
        playerOneScore = score(board)[0]
        playerTwoScore = score(board)[1]
        print("The final scores are, Player 1:", playerOneScore, " and the AI", playerTwoScore)
        if playerOneScore > playerTwoScore:
            print("Player 1 wins!!!")
        elif playerTwoScore > playerOneScore:
            print("AI wins!!!")
        else:
            print("The scores are equal, it is a draw.")

def run_zero_players():
    global board
    board = new_board()
    global currentPlayer
    currentPlayer = 1

    while True:
        print_board(board)
        currentScore = score(board)[currentPlayer - 1]
        testBoard = copy.deepcopy(board)
        moveList = valid_moves(testBoard, currentPlayer)
        bestScore = 0

        for i in range(len(moveList)):
            nextState = next_state(testBoard, currentPlayer, moveList[i])
            testBoard = nextState[0]
            newScore = score(testBoard)[currentPlayer - 1]
            if (newScore - currentScore) > bestScore:
                bestScore = newScore - currentScore
                bestMove = moveList[i]
            testBoard = copy.deepcopy(board)

        nextState = next_state(board, currentPlayer, bestMove)
        print("The AI", currentPlayer, " decided to place a stone on position", reversePosition(bestMove))
        board = nextState[0]
        currentPlayer = nextState[1]
        if valid_moves(board, currentPlayer) == []:
            print("You have run out of moves to player so the game is over!")
            gameOver()

def gameOver():
    playerOneScore = score(board)[0]
    playerTwoScore = score(board)[1]
    print("The final scores are, Player 1:", playerOneScore, " and the AI", playerTwoScore)
    if playerOneScore > playerTwoScore:
        print("AI 1 wins!!!")
    elif playerTwoScore > playerOneScore:
        print("AI 2 wins!!!")
    else:
        print("The scores are equal, it is a draw.")
    exit()

def helpMenu():
    print("This is the list of commands available to players.")
    print("score: Allows players to see the game score.")
    print("valid: Allows players to see a list of available moves to them, also shown by * on the game board.")
    print("board: Allows player to print another copy of the game board.")
    print("quit: Allows the player to exit the game. A winner will be declared.")

    userInput = input('\n' + "Please select a position to place a stone: ")
    return userInput

def specialFunctions(command, board, currentPlayer):
    if command == "score":
        playerOneScore = score(board)[0]
        playerTwoScore = score(board)[1]
        print("The current scores are, Player 1:", playerOneScore, " and the AI:", playerTwoScore)

        userInput = input('\n' + "Please select a position to place a stone: ")
        return userInput
    elif command  == "valid":
        listMoves = valid_moves(board, currentPlayer)
        string = "The moves avaliable to you are "
        for i in range (len(listMoves)):
            string += reversePosition(listMoves[i]) + ", "
        print(string)

        userInput = input('\n' + "Please select a position to place a stone: ")
        return userInput
    elif command == "board":
        print("Here is the current game board")
        print_board(board)

        userInput = input('\n' + "Please select a position to place a stone: ")
        return userInput

def gameStart():
    while True:
        try:
            print("Welcome to Reversi by Adrian Price")
            numPlayer = int(input("Are you playing with 1 or 2 players? "))
            break
        except:
            numPlayer = int(input("Invalid input, please select either 1 or 2 players "))
    if numPlayer == 1:
        run_single_player()
    elif numPlayer == 2:
        run_two_players()
    elif numPlayer == 0:
        run_zero_players()

gameStart()