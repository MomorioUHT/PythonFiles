ls,curr,latest = [],[],[]
avoid = '@#%!^)*(}{'
for i in range(3): ls.append(str(input()))
for i in ls:
    if i.startswith('GUITAR:'): curr = i[8:-2].split(", ")
for i in curr:
    found = 0
    for j in i:
        if j in avoid: found = 1
    if (found == 0): latest.append(i)
    found = 0
    
result = ''
for i in range(0,len(latest)): 
    if i == len(latest)-1: result += latest[i]
    else: result += latest[i] + ", "
print(f"GUITAR:[{result}]")