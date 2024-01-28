board = []

for i in range(5):
    board.append(str(input()))

pins = str(input()).split(" ")

for i in range(5):
    for j in pins:
        if j in board[i]: board[i] = board[i].replace(j, "X")

def check(board): 
    
    #Diagonal Right
    count = 0
    for i in range(5): 
        if board[i][i] == "X": count += 1
        else: break
    if count == 5: return True
    
    #Diagonal Left
    count = 0
    for i in range(5):
        if board[4-i][i] == "X": count += 1
        else: break
    if count == 5: return True
    
    for i in range(5):
        count = 0
        for j in range(5):
            if board[i][j] == "X": count += 1
            else: break
        if count == 5: return True
    
    for i in range(5):
        count = 0
        for j in range(5):
            if board[j][i] == "X": count += 1
            else: break
        if count == 5: return True

    return False
      
for i in board: print(i)
if check(board): print("BINGO")
else: print("YOU LOSE")
