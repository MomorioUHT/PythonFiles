BOARD_SIZE = 8

def bishop_moves(board, x, y):
    for i in range(1, BOARD_SIZE):
        if x + i < BOARD_SIZE and y + i < BOARD_SIZE:
            board[y + i][x + i] = 'X'
        if x - i >= 0 and y + i < BOARD_SIZE:
            board[y + i][x - i] = 'X'
        if x + i < BOARD_SIZE and y - i >= 0:
            board[y - i][x + i] = 'X'
        if x - i >= 0 and y - i >= 0:
            board[y - i][x - i] = 'X'

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != 'X':
                board[i][j] = ' '

    board[y][x] = 'B'
    
    
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
pos_x, pos_y = map(int, input().split())

bishop_moves(board, pos_x, pos_y)

print("  0 1 2 3 4 5 6 7")
print("------------------")
for i in range(BOARD_SIZE):
    print(f"{i}|", end="")
    for j in range(BOARD_SIZE):
        print(f"{board[i][j]}|", end="")
    print("\n------------------")