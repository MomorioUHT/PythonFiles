ls = [int(i) for i in str(input()).split(" ")]
even,odd = [],[]
for i in sorted(ls):
    if i%2 == 0: even.append(i)
    else: odd.append(i)
if len(even) != 0: print(*even)
if len(odd) != 0: print(*odd)