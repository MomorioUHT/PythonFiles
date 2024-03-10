import math
first = [int(i) for i in str(input()).split(" ")]
second = [int(i) for i in str(input()).split(" ")]

a = abs(first[0]-second[0])
b = abs(first[1]-second[1])

print(f"{int(math.factorial(a+b) / (math.factorial(a) * math.factorial(b)))} ways")