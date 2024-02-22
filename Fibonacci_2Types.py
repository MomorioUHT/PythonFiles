#Non Recursive
def fibo(n):
    if n == 1 or n == 2: return 1
    index0,index1 = 1,1
    for i in range(2,n):
        curr = index0 + index1
        index0 = index1
        index1 = curr
    return curr

#Recursive
def fibo_recursive(n):
    if n <= 2: return 1;
    return fibo_recursive(n-1) + fibo_recursive(n-2)

n = int(input())
arr = []
for i in range(1,n+1): arr.append(fibo(i)) #Use Non-Recursive
print(*arr)