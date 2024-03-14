x = int(input())
result = ''
if x <= 0 or x > 52:
    print("-")
else:
    if x%2 == 0:
        for i in range(0,int(x/2)):
            result += chr(i+97) 
            if i != x-1: result += "-"
        for i in range(int(x/2)-1,-1,-1):
            result += chr(i+97) 
            if i != 0: result += "-"        
    else:
        for i in range(0,int(x/2)):
            result += chr(i+97) 
            if i != x-1: result += "-"
        for i in range(int(x/2),-1,-1):
            result += chr(i+97) 
            if i != 0: result += "-"
    print(result)