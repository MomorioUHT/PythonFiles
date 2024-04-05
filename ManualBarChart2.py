digits = [int(n) for n in str(input()).split("-")]
rows = max(digits)
bar_graph = []
for row in range(rows, 0, -1):
    bar_graph.append(['U' if digit >= row else ' ' for digit in digits])
    
i = rows
for row in bar_graph:
    if (len(str(rows)) == 2): print(f"{i:2d}|", end=" ")
    else: print(f"{i}|", end=" ")
    print(' '.join(row))
    i-=1
    
print(f"{'-'*len(str(rows))}-{'-'*((len(digits)*2))}")

data = [int(i) for i in range(len(digits))]
if (len(str(rows)) == 2): print(f"|x|",end=" ")
else: print(f"x|",end=" ")
print(*data)