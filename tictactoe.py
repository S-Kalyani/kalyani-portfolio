def print_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("\n")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def tic_tac_toe():
    board = [str(i) for i in range(9)]
    current_player = 'X'
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over:
        try:
            # Using string concatenation for input prompt
            move = int(input("Player " + current_player + ", enter your move (0-8): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")
            continue

        if 0 <= move <= 8 and board[move] == str(move):
            board[move] = current_player
            print_board(board)

            if check_win(board, current_player):
                # Using string concatenation for win message
                print("Player " + current_player + " wins! Congratulations!")
                game_over = True
            elif check_draw(board):
                print("It's a draw!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. That cell is already taken or out of range. Try again.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        tic_tac_toe()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    tic_tac_toe()
