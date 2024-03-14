x = int(input())
result = ''
if x <= 0 or x > 26:
    print("-")
else:
    for i in range(0,x):
        result += chr(i+97) 
        if i != x-1: result += "-"
    print(result)