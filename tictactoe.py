import os
import sys
import time
from colorama import init, Fore, Style


init(autoreset=True)


board = [" " for _ in range(9)]

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  
    (0, 4, 8), (2, 4, 6)             
]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_board():
    clear()
    print(Fore.CYAN + "\n    TIC TAC TOE\n" + Style.RESET_ALL)
    for i in range(3):
        row = ""
        for j in range(3):
            cell = board[i*3 + j]
            if cell == "X":
                row += Fore.RED + " X " + Style.RESET_ALL
            elif cell == "O":
                row += Fore.GREEN + " O " + Style.RESET_ALL
            else:
                row += Fore.YELLOW + f" {i*3 + j + 1} " + Style.RESET_ALL
            if j < 2:
                row += Fore.CYAN + "|" + Style.RESET_ALL
        print(row)
        if i < 2:
            print(Fore.CYAN + "---+---+---" + Style.RESET_ALL)

def is_winner(player):
    for a, b, c in WIN_COMBOS:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_full():
    return " " not in board

def play_game():
    current_player = "X"
    while True:
        print_board()
        print(Fore.MAGENTA + f"\nPlayer {current_player}'s turn." + Style.RESET_ALL)

        try:
            move = int(input("Choose a position (1-9): ")) - 1
        except ValueError:
            print(Fore.RED + "Invalid input! Enter a number." + Style.RESET_ALL)
            time.sleep(1.2)
            continue

        if move < 0 or move >= 9 or board[move] != " ":
            print(Fore.RED + "Invalid move! Try again." + Style.RESET_ALL)
            time.sleep(1.2)
            continue

        board[move] = current_player

        if is_winner(current_player):
            print_board()
            print(Fore.GREEN + f"\n🎉 Player {current_player} wins! 🎉" + Style.RESET_ALL)
            break
        elif is_full():
            print_board()
            print(Fore.YELLOW + "\nIt's a draw! 🤝" + Style.RESET_ALL)
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
