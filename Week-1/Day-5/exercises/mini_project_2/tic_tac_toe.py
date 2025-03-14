# Function to display the board
def display_board(board):
    print("----+---+----")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("----+---+----")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("----+---+----")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("----+---+----")

# Function to take player input
def player_input(player, board):
    valid = False
    while not valid:
        try:
            position = int(input(f"Player {player}, enter the position (1-9): "))
            if position < 1 or position > 9:
                print("Invalid position. Please choose a number between 1 and 9.")
            elif board[position - 1] != " ":
                print("This position is already taken, try again.")
            else:
                board[position - 1] = player
                valid = True
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Function to check if there's a winner
def check_win(board):
    # Winning combinations (indexes of positions in board)
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
            return True
    return False

# Main function to play the game
def play():
    board = [" "] * 9  # Create an empty board
    current_player = "X"  # X goes first
    game_over = False
    turns = 0

    while not game_over:
        display_board(board)
        player_input(current_player, board)
        turns += 1

        # Check if there's a winner
        if check_win(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif turns == 9:  
            # If all positions are filled
            display_board(board)
            print("It's a tie!")
            game_over = True
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play()
