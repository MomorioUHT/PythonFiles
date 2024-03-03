import math
def isPrime(x: int):
    if (x == 2): return 1
    if (x == 1 or x % 2 == 0): return 0
    for i in range(3, math.ceil(math.sqrt(x))+1, 2):
        if (x % i == 0): return 0
    return 1

ls = [int(i) for i in str(input()).split(" to ")]
for i in range(ls[0],ls[1]+1):
    if (isPrime(i)): print(i, end=" ")
