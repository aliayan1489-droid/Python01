# Simple Tic Tac Toe game in Python (2 players)

board = [" " for _ in range(9)]

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(mark):
    win_cond = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # cols
        [0,4,8], [2,4,6]             # diagonals
    ]
    for combo in win_cond:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == mark:
            return True
    return False


def is_full():
    return " " not in board

def play_game():
    player = "X"
    while True:
        print_board()
        move = input(f"Player {player}, choose position (1-9): ")
        if not move.isdigit() or int(move) not in range(1,10):
            print("Please enter a number between 1 and 9.")
            continue
        move = int(move) - 1
        if board[move] != " ":
            print("That spot is already taken. Try again!")
            continue

        board[move] = player

        if check_winner(player):
            print_board()
            print(f"🎉 Player {player} wins!")
            break
        if is_full():
            print_board()
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

play_game()
