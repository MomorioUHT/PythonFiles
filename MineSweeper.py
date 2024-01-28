dimensions = str(input()).split("x") 
amount = int(input())
bomb,board = [],[] 

for i in range(0,amount):
    a = str(input()).split(",")
    bomb.append(a)
    
for i in range(0, int(dimensions[0])): board.append(list("0"*int(dimensions[1]))) 
for i in bomb: board[int(i[0])][int(i[1])] = "*"

for b in range(0, int(dimensions[0])): 
    for a in range(0, int(dimensions[1])): 
        if board[b][a] != "*": 
            #4 Corner Checks
            if b == 0 and a == 0: #Left Up
                count = 0
                if board[0][1] == "*": count +=1
                if board[1][0] == "*": count +=1
                if board[1][1] == "*": count += 1
                board[b][a] = count
            elif b == 0 and a == int(dimensions[1])-1: #Right Up
                count = 0
                if board[0][int(dimensions[1])-2] == "*": count +=1
                if board[1][int(dimensions[1])-2] == "*": count += 1
                if board[1][int(dimensions[1])-1] == "*": count +=1
                board[b][a] = count
            elif b == int(dimensions[0])-1 and a == 0: #Left Down
                count = 0
                if board[int(dimensions[0])-2][1] == "*": count +=1
                if board[int(dimensions[0])-2][0] == "*": count += 1
                if board[int(dimensions[0])-1][1] == "*": count +=1
                board[b][a] = count
            elif b == int(dimensions[0])-1 and a == int(dimensions[1])-1: #Right Down
                count = 0
                if board[int(dimensions[0])-2][int(dimensions[1])-1] == "*": count +=1
                if board[int(dimensions[0])-2][int(dimensions[1])-2] == "*": count += 1
                if board[int(dimensions[0])-1][int(dimensions[1])-2] == "*": count +=1
                board[b][a] = count
            #4 Boarder Check
            elif b == 0: #Upper Boarder
                count = 0
                if board[0][int(a)-1] == "*": count += 1   
                if board[0][int(a)+1] == "*": count += 1   
                if board[1][int(a)-1] == "*": count += 1   
                if board[1][int(a)] == "*": count += 1   
                if board[1][int(a)+1] == "*": count += 1   
                board[b][a] = count
            elif b == int(dimensions[0])-1: #Lower Boarder
                count = 0
                if board[int(dimensions[0])-1][int(a)-1] == "*": count += 1   
                if board[int(dimensions[0])-1][int(a)+1] == "*": count += 1   
                if board[int(dimensions[0])-2][int(a)-1] == "*": count += 1   
                if board[int(dimensions[0])-2][int(a)] == "*": count += 1   
                if board[int(dimensions[0])-2][int(a)+1] == "*": count += 1   
                board[b][a] = count
            elif a == int(dimensions[1])-1: #Right Boarder 
                count = 0
                if board[int(b)-1][int(a)] == "*": count += 1  
                if board[int(b)+1][int(a)] == "*": count += 1 
                if board[int(b)-1][int(a)-1] == "*": count += 1  
                if board[int(b)][int(a)-1] == "*": count += 1 
                if board[int(b)+1][int(a)-1] == "*": count += 1 
                board[b][a] = count
            elif a == 0: #Left Boarder 
                count = 0
                if board[int(b)-1][0] == "*": count += 1  
                if board[int(b)+1][0] == "*": count += 1  
                if board[int(b)-1][1] == "*": count += 1
                if board[int(b)][1] == "*": count += 1 
                if board[int(b)+1][1] == "*": count += 1 
                board[b][a] = count
            #Inboard Safe
            else:
                count = 0
                if board[b-1][a-1] == "*": count += 1
                if board[b-1][a] == "*": count += 1
                if board[b-1][a+1] == "*": count += 1
                if board[b][a-1] == "*": count += 1
                #NO b,a pairs
                if board[b][a+1] == "*": count += 1
                if board[b+1][a-1] == "*": count += 1
                if board[b+1][a] == "*": count += 1
                if board[b+1][a+1] == "*": count += 1
                board[b][a] = count
for i in board: print(*i, sep="")
