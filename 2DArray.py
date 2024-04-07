board = []
dim = [int(i) for i in str(input()).split("x")]
num = dim[0]*dim[1]
count = 1
for i in range(dim[1]):
    board.append([])
    for j in range(dim[0]):
        board[i].append(count)
        count+=1

for i in range(dim[1]):
    for j in range(dim[0]):
        number = int(board[i][j])
        if num >=100: 
            if j == dim[0]-1: print(f"{number:3d}", end="")
            else: print(f"{number:3d} ", end="")
        elif num >= 10: 
            if j == dim[0]-1: print(f"{number:2d}", end="")
            else: print(f"{number:2d} ", end="")
        else: 
            if j == dim[0]-1: print(f"{number}", end="")
            else: print(f"{number} ", end="")
    print("")