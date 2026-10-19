import random
from logo import LOGO


WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def print_board(board):
    for i in range(0, 9, 3):
        row = board[i:i+3]
        print(" | ".join(row))
        if i < 6:
            print("--+---+--")


def get_move(board, player):
    while True:
        try:
            position = int(input(f"Player {player}, choose a position (1-9): "))

            if position < 1 or position > 9:
                raise ValueError
            elif board[position - 1] != " ":
                print("That spot is taken, try another")
            else:
                return position - 1

        except ValueError:
            print("Please type a number from 1 to 9")


def computer_move(board):
    while True:
        comp_pos = random.randint(0, 8)
        if board[comp_pos] == " ":
            return comp_pos


def check_winner(board):
    for a, b, c in WINNING_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return True
    return False


def is_draw(board):
    return " " not in board


def play_game():
    board = [" "] * 9
    player = "X"

    while True:
        human = input("Player, choose X or O: ").upper()
        if human == "X" or human == "O":
            break
        print("Please type X or O")

    while True:
        print_board(board)

        if player == human:
            move = get_move(board, player)
        else:
            move = computer_move(board)
            print(f"Computer chose a position: {move + 1}")

        board[move] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        else:
            if player == "X":
                player = "O"
            else:
                player = "X"

print(LOGO)

while True:
    play_game()
    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        break