original = []
Transpose = [] 
    
while True:
    x = str(input()).split(" ")
    if x == ["-1"]: break
    else: original.append(x)

original_x = len(original[0])
original_y = len(original)
transpose_x = original_y 
transpose_y = original_x

for i in range(0,transpose_y): 
    temp = []
    for j in range(0,transpose_x): temp.append(1)
    Transpose.append(temp)
    
for i in range(0,transpose_y):
    for j in range(0,transpose_x): Transpose[i][j] = original[j][i]
        
for i in Transpose: print(*i) 