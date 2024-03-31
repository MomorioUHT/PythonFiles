board = []
opponent,your = 0,0
for i in range(8):
    temp = [i for i in str(input())]
    for j in temp: board.append(j)
for i in board:
    if i == "P": your+=1
    if i == "p": opponent+=1
    if i == "N": your+=3
    if i == "n": opponent+=3
    if i == "B": your+=3
    if i == "b": opponent+=3
    if i == "R": your+=5
    if i == "r": opponent+=5
    if i == "Q": your+=9
    if i == "q": opponent+=9
result = your-opponent
if (result == 0): print("equal")
else: print(result)