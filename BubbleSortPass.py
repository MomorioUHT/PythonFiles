ls = [int(i) for i in str(input()).split(" ")]
n = len(ls)
for i in range(1,n):
    if ls == sorted(ls): break
    for j in range(0,n-1):
        if ls[j] > ls[j+1]: 
            ls[j],ls[j+1] = ls[j+1],ls[j]
    print(*ls)