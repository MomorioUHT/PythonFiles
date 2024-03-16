result = ''
while (True):
    x = str(input())
    if x == "-1": break 
    result += x.split(" ")[0]
print(result)