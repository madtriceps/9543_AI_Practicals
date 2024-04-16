# Constants for player symbols
EMPTY = 0
X = 1
O = 2

# Constants for game result
DRAW = 0
X_WINS = 1
O_WINS = 2
IN_PROGRESS = 3

# Define winning combinations
WINNING_COMBINATIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Main function to play the game
def main():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]  # Initialize the board
    current_player = X  # X always starts
    winner = IN_PROGRESS

    while winner == IN_PROGRESS:
        print_board(board)
        if current_player == X:
            move = get_player_move(board)
            board[move[0]][move[1]] = X
        else:
            move = get_computer_move(board)
            board[move[0]][move[1]] = O
        winner = check_winner(board)
        current_player = O if current_player == X else X  # Switch players

    print_board(board)
    if winner == X_WINS:
        print("X wins!")
    elif winner == O_WINS:
        print("O wins!")
    else:
        print("It's a draw!")

# Function to get the player's move from the console
def get_player_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == EMPTY:
                return row, col
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get the computer's move using minimax algorithm
def get_computer_move(board):
    best_move = (-1, -1)
    best_score = float('-inf')

    # Iterate over all empty cells to simulate possible moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = O  # Simulate the move for the computer
                score = minimax(board, 0, False)  # Evaluate the move using minimax
                board[i][j] = EMPTY  # Undo the move

                # Update the best move if a higher score is found
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing):
    result = check_winner(board)
    if result != IN_PROGRESS:
        return calculate_score(result, depth)

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = X
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

# Function to score the game state based on the depth
def calculate_score(result, depth):
    if result == X_WINS:
        return -10 + depth
    elif result == O_WINS:
        return 10 - depth
    return 0

# Function to check if there is a winner or if it's a draw
def check_winner(board):
    # Check for winning combinations
    for combination in WINNING_COMBINATIONS:
        if board[combination[0] // 3][combination[0] % 3] != EMPTY and \
                board[combination[0] // 3][combination[0] % 3] == board[combination[1] // 3][combination[1] % 3] and \
                board[combination[1] // 3][combination[1] % 3] == board[combination[2] // 3][combination[2] % 3]:
            return X_WINS if board[combination[0] // 3][combination[0] % 3] == X else O_WINS

    # Check for draw
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return IN_PROGRESS  # Game still in progress
    return DRAW  # If no empty cells left, it's a draw

# Function to print the current state of the board
def print_board(board):
    print("  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            if board[i][j] == X:
                print("X", end=" ")
            elif board[i][j] == O:
                print("O", end=" ")
            else:
                print("-", end=" ")
        print()

if __name__ == "__main__":
    main()
