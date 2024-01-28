#Chess moves

def MarkMoves(piece: str, x: int, y: int):
    if piece == "Queen":
        for i in range(0,8):
            if (y+i < 8 and x+i < 8): chessboard[y+i][x+i] = "X"
            if (y-i >= 0 and x-i >= 0): chessboard[y-i][x-i] = "X"
            if (y+i < 8 and x-i >= 0): chessboard[y+i][x-i] = "X"
            if (y-i >= 0 and x+i < 8): chessboard[y-i][x+i] = "X" 
        for i in range(0,8):
            if (y-i >= 0): chessboard[y-i][x] = "X"
            if (y+i < 8): chessboard[y+i][x] = "X"
            if (x-i >= 0): chessboard[y][x-i] = "X"
            if (x+i < 8): chessboard[y][x+i] = "X"    
        chessboard[y][x] = "Q"
    elif piece == "Bishop":
        for i in range(0,8):
            if (y+i < 8 and x+i < 8): chessboard[y+i][x+i] = "X"
            if (y-i >= 0 and x-i >= 0): chessboard[y-i][x-i] = "X"
            if (y+i < 8 and x-i >= 0): chessboard[y+i][x-i] = "X"
            if (y-i >= 0 and x+i < 8): chessboard[y-i][x+i] = "X" 
        chessboard[y][x] = "B"
    elif piece == "Rook":
        for i in range(0,8):
            if (y-i >= 0): chessboard[y-i][x] = "X"
            if (y+i < 8): chessboard[y+i][x] = "X"
            if (x-i >= 0): chessboard[y][x-i] = "X"
            if (x+i < 8): chessboard[y][x+i] = "X"  
        chessboard[y][x] = "R"
    elif piece == "King":
        if (y-1 >= 0): chessboard[y-1][x] = "X"
        if (y+1 < 8): chessboard[y+1][x] = "X"
        if (x-1 >= 0): chessboard[y][x-1] = "X"
        if (x+1 < 8): chessboard[y][x+1] = "X" 
        if (y+1 < 8 and x+1 < 8): chessboard[y+1][x+1] = "X"
        if (y-1 >= 0 and x-1 >= 0): chessboard[y-1][x-1] = "X"
        if (y+1 < 8 and x-1 >= 0): chessboard[y+1][x-1] = "X"
        if (y-1 >= 0 and x+1 < 8): chessboard[y-1][x+1] = "X" 
        chessboard[y][x] = "K"
    elif piece == "Knight":
        if (y+2 < 8 and x+1 < 8): chessboard[y+2][x+1] = "X"
        if (y-2 >= 0 and x-1 >= 0): chessboard[y-2][x-1] = "X"
        if (y+1 < 8 and x-2 >= 0): chessboard[y+1][x-2] = "X"
        if (y-1 >= 0 and x+2 < 8): chessboard[y-1][x+2] = "X"
        if (y+1 < 8 and x+2 < 8): chessboard[y+1][x+2] = "X"
        if (y-1 >= 0 and x-2 >= 0): chessboard[y-1][x-2] = "X"
        if (y+2 < 8 and x-1 >= 0): chessboard[y+2][x-1] = "X"
        if (y-2 >= 0 and x+1 < 8): chessboard[y-2][x+1] = "X"
        chessboard[y][x] = "K"
    elif piece == "Pawn":
        if (y-1 >= 0): chessboard[y-1][x] = "X"
        chessboard[y][x] = "P"
    
chessboard = [[" "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "],
              ]

piece = str(input())
ls = [int(i) for i in str(input()).split(" ")]
MarkMoves(piece, ls[0], ls[1])

print("  0 1 2 3 4 5 6 7 ")
print("------------------")
for i in range(8):
    print(f"{i}|", end="")
    for j in range(8):
        print(f"{chessboard[i][j]}|", end="")
    print("\n------------------")
    