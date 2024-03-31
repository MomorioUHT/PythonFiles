context = ""
while True:
    x = str(input()).split(" ")
    if x[0] == "EXIT": break
    
    if x[0] == "INSERT": context += x[1]
    elif x[0] == "DELETE": context = context[0:-1]
    elif x[0] == "REMOVE": context = context.replace(x[1],"")
    elif x[0] == "ROTATE": context = context[::-1]
print(context)