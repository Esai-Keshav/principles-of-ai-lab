# Tic-Tac-Toe Board
board = [" " for _ in range(9)]


# Function to print the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Function to check if the board is full
def is_full(board):
    return " " not in board


# Function to check if a player has won
def is_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False


# Min-Max algorithm
def minimax(board, depth, is_maximizing):
    scores = {
        "X": 1,
        "O": -1,
        "Tie": 0,
    }

    if is_winner(board, "X"):
        return scores["X"] - depth
    if is_winner(board, "O"):
        return scores["O"] + depth
    if is_full(board):
        return scores["Tie"]

    if is_maximizing:
        best_score = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


# Function to find the best move
def find_best_move(board):
    best_move = -1
    best_score = float("-inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


# Main game loop
while True:
    print_board()
    move = int(input("Enter your move (0-8): "))

    if board[move] != " ":
        print("Invalid move. Try again.")
        continue

    board[move] = "O"

    if is_winner(board, "O"):
        print_board()
        print("You win!")
        break

    if is_full(board):
        print_board()
        print("It's a tie!")
        break

    best_move = find_best_move(board)
    board[best_move] = "X"

    if is_winner(board, "X"):
        print_board()
        print("Computer wins!")
        break

    if is_full(board):
        print_board()
        print("It's a tie!")
        break
