board = []
for i in range(9):
    board.append(str(input()).split(" "))
target = str(input())
for i in range(9):
    for j in range(9):
        if board[i][j] != target: board[i][j] = " "
    
print("---------------------")
print("|    BLOCK PARTY    |")
print("---------------------")
for i in board:
    result = ''
    for j in i:
        result += j + " "
    print(f"| {result}|")
print("---------------------")