PLAYER = "X"
AI = "O"

player_score = 0

#PRINT BOARD
def print_board():
    for i in range(3):
        row = " | ".join([cell if cell != "" else " " for cell in board[i]])
        print(row)
        if i < 2:
            print("-" * 9)

# CHECK WIN 
def check_winner(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != "":
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != "":
            return b[0][i]

    if b[0][0] == b[1][1] == b[2][2] != "":
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != "":
        return b[0][2]

    return None

#CHECK FULL
def is_full(b):
    for row in b:
        if "" in row:
            return False
    return True

# MINIMAX
def minimax(b, is_maximizing):
    winner = check_winner(b)

    if winner == AI:
        return 1
    elif winner == PLAYER:
        return -1
    elif is_full(b):
        return 0

    if is_maximizing:
        best_score = -100
        for i in range(3):
            for j in range(3):
                if b[i][j] == "":
                    b[i][j] = AI
                    score = minimax(b, False)
                    b[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 100
        for i in range(3):
            for j in range(3):
                if b[i][j] == "":
                    b[i][j] = PLAYER
                    score = minimax(b, True)
                    b[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

#AI MOVE
def ai_move():
    best_score = -100
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = AI
                score = minimax(board, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)

    if move:
        i, j = move
        board[i][j] = AI
        print(f"\n AI played at ({i+1}, {j+1})")

while True:
    board = [["" for _ in range(3)] for _ in range(3)]

    print("\n New Game Started!")

    print("\n Instructions:")
    print("Type 'quit' anytime to stop the current game.")
    print("After a game ends:")
    print("Type 'continue' → play next game")
    print("Type 'end' → reset score and start fresh\n")

    while True:
        print("\nCurrent Board:")
        print_board()

        row_input = input("Enter row (1-3) or type quit: ")

        if row_input.lower() == "quit":
            print("\n⚠ Game stopped!")
            break

        col_input = input("Enter col (1-3): ")

        if col_input.lower() == "quit":
            print("\n⚠ Game stopped!")
            break

        try:
            row = int(row_input) - 1
            col = int(col_input) - 1
        except:
            print("Invalid input! Try again.")
            continue

        if row not in range(3) or col not in range(3) or board[row][col] != "":
            print("Invalid move! Try again.")
            continue

        board[row][col] = PLAYER

        if check_winner(board):
            print_board()
            print("\n You win!")
            player_score += 1
            break

        if is_full(board):
            print_board()
            print("\n It's a draw!")
            break

        ai_move()

        if check_winner(board):
            print_board()
            print("\n AI wins!")
            player_score -= 1
            break

        if is_full(board):
            print_board()
            print("\n It's a draw!")
            break

    #AFTER GAME
    print("\n Final Score:", player_score)

    while True:
        print("\n What do you want to do next?")
        print("Type 'continue' → play next game")
        print("Type 'end' → reset score and start fresh")

        choice = input("Enter your choice: ")

        if choice.lower() == "continue":
            break

        elif choice.lower() == "end":
            player_score = 0
            print("\n Score reset! Starting fresh...\n")
            break

        else:
            print("Invalid input! Try again.")
