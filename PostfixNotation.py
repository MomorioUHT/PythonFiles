ls = [i for i in str(input()).split(" ")]
while len(ls) >= 2:
    for i in range(0,len(ls)):
        if ls[i] == "+": 
            ls[i] = int(ls[i-2]) + int(ls[i-1])
            break
        elif ls[i] == "-": 
            ls[i] = int(ls[i-2]) - int(ls[i-1])
            break
        elif ls[i] == "*": 
            ls[i] = int(ls[i-2]) * int(ls[i-1])
            break
        elif ls[i] == "/": 
            ls[i] = int(ls[i-2]) / int(ls[i-1])
            break
    ls.pop(i-1)
    ls.pop(i-2) 
print(f"{ls[0]:.2f}")