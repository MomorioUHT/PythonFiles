ls = []
while (True):
    x = str(input())
    if x == "-1": break
    if x.isdigit(): ls.append(int(x))
if max(ls) >= 10:
    for i in ls: print(f"{i:2d} | {'[]'*i}")
else: 
    for i in ls: print(f"{i} | {'[]'*i}")