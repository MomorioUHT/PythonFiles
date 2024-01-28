text = str(input())
cursor = int(input())

listoftext = (text.lstrip().rstrip()).split(" ")

if len(text) == 1: print(text)
else:
    final = ''
    start = 0
    end = 0
    for i in range(cursor,len(text)-1):
        if text[i].isspace(): 
            end = i
            break
    for i in range(cursor,0,-1):
        if text[i].isspace(): 
            start = i+1
            break

    if end != 0: final = text[start:end]
    if end == 0: final = text[start::]
    
    print(final)
    print(listoftext.index(final))