# Tic Tac Toe Game in Python (Console)

board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_win(player):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def check_draw():
    return ' ' not in board

print("🎮 TIC TAC TOE GAME")
print("Player 1 = X | Player 2 = O")
print("Positions: 1 to 9")

print_board()

current_player = 'X'

while True:
    move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

    if board[move] != ' ':
        print("❌ Position already taken. Try again.")
        continue

    board[move] = current_player
    print_board()

    if check_win(current_player):
        print(f"🎉 Player {current_player} Wins!")
        break

    if check_draw():
        print("🤝 It's a Draw!")
        break

    current_player = 'O' if current_player == 'X' else 'X'
