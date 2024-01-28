dimension = [int(i) for i in str(input()).split("x")]
board = []
lines = []

while True:
    x = [int(i) for i in str(input()).split(" ")]
    if x == [0]: break
    board.append(x)

for i in range(0,len(board)-dimension[0]+1):
    temp = []
    for j in range(0,len(board[0])-dimension[1]+1):
        avg = 0
        for k in range(dimension[1]):
            for l in range(dimension[0]):
                avg += board[k+i][l+j]
        temp.append(f"{avg/(dimension[0]*dimension[1]):.2f}")
    lines.append(temp)

for i in lines: print(*i)

