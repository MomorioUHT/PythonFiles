left,right = [],[]
while True:
    x = str(input())
    if x == '-1': break
    left.append(x[:x.find("=")].rstrip()); right.append(x[x.find("=")+1:].lstrip())
maxlength = max(left, key=len)   
for i in range(0,len(left)): print(f"{left[i].rjust(len(maxlength), ' ')} = {right[i]}")