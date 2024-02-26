ls = [int(i) for i in str(input()).split(" ")]
ls.sort()
max = 0
for i in range(0,len(ls)-1):
    result = ls[i+1] - ls[i] - 1
    if result > max: max = result
if max == 1: print(f"{max} day")
else: print(f"{max} days")