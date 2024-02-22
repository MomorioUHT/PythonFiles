x = int(input())
ans = [[1]]
for i in range(x-1):
    temp = [0] + ans[-1] + [0]
    row = []
    for j in range(len(ans[-1])+1):
        row.append(temp[j]+temp[j+1])
    ans.append(row)
for i in ans: print(*i)